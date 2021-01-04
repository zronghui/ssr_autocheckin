import requests
import json
import time
from icecream import ic
from config import config

requests.packages.urllib3.disable_warnings()


def checkin(base_url, email, password):
    email = email.split('@')
    email = email[0] + '%40' + email[1]
    session = requests.session()
    session.get(base_url, verify=False)
    login_url = base_url + '/auth/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    post_data = 'email=' + email + '&passwd=' + password + '&code='
    post_data = post_data.encode()
    response = session.post(login_url, post_data,
                            headers=headers, verify=False)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Referer': base_url + '/user'
    }
    response = session.post(base_url + '/user/checkin',
                            headers=headers, verify=False)
    print(json.loads(response.text))


for c in config:
    base_url, email, password = c['base_url'], c['email'], c['password']
    while True:
        try:
            ic(base_url, email, password)
            checkin(base_url, email, password)
        except Exception as e:
            print(e)
            time.sleep(3)
            continue
        break
