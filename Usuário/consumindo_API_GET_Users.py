import json
import requests

URL = 'http://127.0.0.1:5000/'

endpoint = URL + 'usuarios/2'


resposta = requests.request('GET', endpoint)

status = resposta.status_code
resp = resposta.json()

print(status)
print(resp)
