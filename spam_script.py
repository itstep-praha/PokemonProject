import requests


url = 'http://127.0.0.1:8000/pokemon/'


for i in range(1_000_000):
    response = requests.get(url)
    print(response, response.elapsed)

