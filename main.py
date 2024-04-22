import requests
import csv
import pandas as pd
import os


URL = "http://202.90.198.40/sismon-slmon2/data/slmon.all.laststatus.json?_="

def main():
    # timestamp = round(time.time() * 1000)

    sites = pd.read_csv('daftar-site-t3s.csv')
    sites = set(sites['Station'])

    response = requests.get(f"{URL}")

    if response.status_code != 200:
        return "Server Error"

    data = response.json()

    data_dirs = os.listdir("data")

    if len(data_dirs) == 0:
        for site in sites:
            with open(f'data/{site}.csv', mode='w', newline="") as site_writer:
                writer = csv.writer(site_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(["time", "ch1", "ch2", 'ch3', 'ch4', 'ch5', 'ch6', 'timech1', 'timech2', 'timech3',
                                    'timech4', 'timech5', 'timech6', 'latency1', 
                                    'latency2', 'latency3', 'latency4', 'latency5', 
                                    'latency6'])

    for item in data['features']:
        if item['properties']['sta'] in sites:
            site = item['properties']['sta']
            with open(f'data/{site}.csv', mode='a', newline="") as site_writer:
                writer = csv.writer(site_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([item['properties']['time'], item['properties']['ch1'], item['properties']['ch2'], item['properties']['ch3'], item['properties']['ch4'], 
                                    item['properties']['ch5'], item['properties']['ch6'], item['properties']['timech1'], item['properties']['timech2'], item['properties']['timech3'],
                                    item['properties']['timech4'], item['properties']['timech5'], item['properties']['timech6'], item['properties']['latency1'], 
                                    item['properties']['latency2'], item['properties']['latency3'], item['properties']['latency4'], item['properties']['latency5'], 
                                    item['properties']['latency6']])
if __name__ == '__main__':
    main()