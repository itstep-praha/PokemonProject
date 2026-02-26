import re
import requests

base_url = 'https://vbrothanek.eu.pythonanywhere.com'
# base_url = 'http://127.0.0.1:8000'

def spam1():

    url =  base_url + '/accounts/login/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
        'Referer': base_url,
    }

    client = requests.Session()
    resp = client.get(url) 
    csrftoken = client.cookies['csrftoken']
    headers['X-CSRFToken'] = csrftoken

    regex = '<input type="hidden" name="csrfmiddlewaretoken" value="(.+)">'
    match = re.search(regex, resp.text)
    token = match.group(1)



    login_url = base_url + '/admin/login/'

    for i in range(1000):
        resp = client.post(login_url, data={
            'csrfmiddlewaretoken': token,
            'login': 'admin',
            'password': 'adminpass',
        },
        headers=headers)

        print(i, resp)


spam1()


