import requests
import schedule
import time

def job():
    result = requests.get('https://api.countapi.xyz/hit/valmir.junior.redirecionamento/development.acessos')
    print(result.text)

schedule.every(5).seconds.do(job)

while 1:
    schedule.run_pending()
