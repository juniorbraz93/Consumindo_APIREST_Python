import json
import requests

URL = 'http://127.0.0.1:5000/'

endpoint = URL + 'cadastro'

body = {
    'email': 'jbraz.est@gmail.com',
    'password': '123123'
}

headers = {
    'Content-Type': 'application/json'
}

resposta = requests.request('POST', endpoint, json=body, headers=headers)

status = resposta.status_code
resp = resposta.json()

print(status)
print(resp)
