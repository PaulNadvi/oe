import requests
import datetime

def main():
    t = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    r = requests.get('https://energypay.oe.if.ua:8889/GAVTurnOff/'
                     'CityFilterPReport?cityList=11726&remList=nad_p&dBegin=&dEnd=&allRem=false', verify=False)
    with open(f'files/{t}.html', 'bw') as f:
        f.write(r.content)

if __name__ == "__main__":
    main()