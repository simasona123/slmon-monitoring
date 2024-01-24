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
        elif item['properties']['sta'] == 'ARKPI':
            tmp['ARKPI'] = item['properties']
        elif item['properties']['sta'] == 'BAKI':
            tmp['BAKI'] = item['properties']
        elif item['properties']['sta'] == 'BDCM':
            tmp['BDCM'] = item['properties']
        elif item['properties']['sta'] == 'CGJI':
            tmp['CGJI'] = item['properties']


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
    
    with open('arkpi.csv', mode='a') as arkpi:
        arkpi_writer = csv.writer(arkpi, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        arkpi_writer.writerow([tmp['ARKPI']['time'], tmp['ARKPI']['ch1'], tmp['ARKPI']['ch2'], tmp['ARKPI']['ch3'], tmp['ARKPI']['ch4'], 
                              tmp['ARKPI']['ch5'], tmp['ARKPI']['ch6'], tmp['ARKPI']['timech1'], tmp['ARKPI']['timech2'], tmp['ARKPI']['timech3'],
                              tmp['ARKPI']['timech4'], tmp['ARKPI']['timech5'], tmp['ARKPI']['timech6'], tmp['ARKPI']['latency1'], 
                              tmp['ARKPI']['latency2'], tmp['ARKPI']['latency3'], tmp['ARKPI']['latency4'], tmp['ARKPI']['latency5'], 
                              tmp['ARKPI']['latency6']])
    
    with open('baki.csv', mode='a') as baki:
        baki_writer = csv.writer(baki, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        baki_writer.writerow([tmp['BAKI']['time'], tmp['BAKI']['ch1'], tmp['BAKI']['ch2'], tmp['BAKI']['ch3'], tmp['BAKI']['ch4'], 
                              tmp['BAKI']['ch5'], tmp['BAKI']['ch6'], tmp['BAKI']['timech1'], tmp['BAKI']['timech2'], tmp['BAKI']['timech3'],
                              tmp['BAKI']['timech4'], tmp['BAKI']['timech5'], tmp['BAKI']['timech6'], tmp['BAKI']['latency1'], 
                              tmp['BAKI']['latency2'], tmp['BAKI']['latency3'], tmp['BAKI']['latency4'], tmp['BAKI']['latency5'], 
                              tmp['BAKI']['latency6']])
    
    with open('bdcm.csv', mode='a') as bdcm:
        bdcm_writer = csv.writer(bdcm, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        bdcm_writer.writerow([tmp['BDCM']['time'], tmp['BDCM']['ch1'], tmp['BDCM']['ch2'], tmp['BDCM']['ch3'], tmp['BDCM']['ch4'], 
                              tmp['BDCM']['ch5'], tmp['BDCM']['ch6'], tmp['BDCM']['timech1'], tmp['BDCM']['timech2'], tmp['BDCM']['timech3'],
                              tmp['BDCM']['timech4'], tmp['BDCM']['timech5'], tmp['BDCM']['timech6'], tmp['BDCM']['latency1'], 
                              tmp['BDCM']['latency2'], tmp['BDCM']['latency3'], tmp['BDCM']['latency4'], tmp['BDCM']['latency5'], 
                              tmp['BDCM']['latency6']])
    
    with open('cgji.csv', mode='a') as CGJI:
        cgji_writer = csv.writer(CGJI, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        cgji_writer.writerow([tmp['CGJI']['time'], tmp['CGJI']['ch1'], tmp['CGJI']['ch2'], tmp['CGJI']['ch3'], tmp['CGJI']['ch4'], 
                              tmp['CGJI']['ch5'], tmp['CGJI']['ch6'], tmp['CGJI']['timech1'], tmp['CGJI']['timech2'], tmp['CGJI']['timech3'],
                              tmp['CGJI']['timech4'], tmp['CGJI']['timech5'], tmp['CGJI']['timech6'], tmp['CGJI']['latency1'], 
                              tmp['CGJI']['latency2'], tmp['CGJI']['latency3'], tmp['CGJI']['latency4'], tmp['CGJI']['latency5'], 
                              tmp['CGJI']['latency6']])
    
if __name__ == '__main__':
    main()