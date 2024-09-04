import requests
import logging
import sqlite3
from datetime import datetime, timedelta
import traceback

def main():
    # Configure the logging to a file
    logging.basicConfig(filename='slmon-bali.log', level=logging.DEBUG, 
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    URL = "http://36.92.49.116:8899/slmon2bali/data/slmon.all.laststatus.json"

    conn = sqlite3.connect('slmon-bali.db')

    # Create a cursor object
    cur = conn.cursor()

    try:
        response = requests.get(f"{URL}")
        if response.status_code != 200:
            logging.error(f"Server status code = {response.status_code}")
        else:
            data = response.json()
            print('response json')
            timestamp = datetime.now()
            print(timestamp)
            for site in data['features']:
                properties = site['properties']
                latency = check_latency(properties)
                cur.execute('''
                INSERT INTO slmons (timestamp, sitename, timech, latency, status) 
                VALUES (?, ?, ?, ?, ?)
                ''', (timestamp, properties['sta'], 
                      properties[f'timech{latency[1]}'], 
                      latency[0], properties[f'color{latency[1]}']))
            conn.commit()
        check_retention(conn, cur)

    except Exception as error:
        logging.error(f"{error} | {traceback.format_exc()}")

    finally:
        conn.close()


def check_latency(site):
    times = {
        's' : 1,
        'm' : 60,
        'h' : 3600,
        'd' : 3600*60,
    }
    latencies = [site['latency1'], site['latency2'], site['latency3'], 
           site['latency4'], site['latency5'], site['latency6'] 
        ]
    
    latency_minimum = -1
    latency_index = 0

    for i in range(0, len(latencies)):
        if latencies[i] == 'NA' : continue
        latency = int(latencies[i][:-1]) * times[latencies[i][-1]]
        if latency_minimum == -1 or latency < latency_minimum:
            latency_minimum = latency
            latency_index = i

    return [latency_minimum, latency_index+1]

def check_retention(conn, cur):
    cur.execute("""SELECT * FROM slmons ORDER BY timestamp DESC LIMIT 1""")
    first_row = cur.fetchone()
    cur.execute("""SELECT * FROM slmons ORDER BY timestamp LIMIT 1""")
    last_row = cur.fetchone()
    date_format = '%Y-%m-%d %H:%M:%S.%f'
    last_date = datetime.strptime(first_row[0], date_format)
    first_date = datetime.strptime(last_row[0], date_format)
    diff_time = last_date - first_date
    print(first_date, last_date, diff_time)
    if diff_time > timedelta(days=90):
        print('maksimum retention')
        retention = first_date + timedelta(days=1)
        cur.execute("""
        DELETE FROM slmons where timestamp < ?
        """, (retention,))
        conn.commit()
    
main()




