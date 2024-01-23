import requests
import time 
import csv


URL = "http://202.90.198.40/sismon-slmon2/data/slmon.all.laststatus.json?_="

def main():
    timestamp = round(time.time() * 1000)
    response = requests.get(f"{URL}{timestamp}")

    if response.status_code != 200:
        return "Server Error"

    tmp = {}

    data = response.json()
    for item in data['features']:
        if item['properties']['sta'] == 'TNGI': 
            tmp['TNGI'] = item['properties']
        elif item['properties']['sta'] == 'YOGI':
            tmp['YOGI'] = item['properties']

    with open('tngi.csv', mode='a') as tngi:
        tngi_writer = csv.writer(tngi, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        tngi_writer.writerow([tmp['TNGI']['time'], tmp['TNGI']['ch1'], tmp['TNGI']['ch2'], tmp['TNGI']['ch3'], tmp['TNGI']['ch4'], 
                              tmp['TNGI']['ch5'], tmp['TNGI']['ch6'], tmp['TNGI']['timech1'], tmp['TNGI']['timech2'], tmp['TNGI']['timech3'],
                              tmp['TNGI']['timech4'], tmp['TNGI']['timech5'], tmp['TNGI']['timech6'], tmp['TNGI']['latency1'], 
                              tmp['TNGI']['latency2'], tmp['TNGI']['latency3'], tmp['TNGI']['latency4'], tmp['TNGI']['latency5'], 
                              tmp['TNGI']['latency6']])

    with open('yogi.csv', mode='a') as yogi:
        yogi_writer = csv.writer(yogi, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        yogi_writer.writerow([tmp['YOGI']['time'], tmp['YOGI']['ch1'], tmp['YOGI']['ch2'], tmp['YOGI']['ch3'], tmp['YOGI']['ch4'], 
                              tmp['YOGI']['ch5'], tmp['YOGI']['ch6'], tmp['YOGI']['timech1'], tmp['YOGI']['timech2'], tmp['YOGI']['timech3'],
                              tmp['YOGI']['timech4'], tmp['YOGI']['timech5'], tmp['YOGI']['timech6'], tmp['YOGI']['latency1'], 
                              tmp['YOGI']['latency2'], tmp['YOGI']['latency3'], tmp['YOGI']['latency4'], tmp['YOGI']['latency5'], 
                              tmp['YOGI']['latency6']])
    

if __name__ == '__main__':
    main()