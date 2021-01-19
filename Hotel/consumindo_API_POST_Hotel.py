import json
import requests

URL = 'http://127.0.0.1:5000/'


token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODYyMDM5NzIsIm5iZiI6MTU4NjIwMzk3MiwianRpIjoiNzAyYzdhYjItNWY4OC00ZWIzLTk3ZjAtYzFiYjRkY2RmZDBjIiwiZXhwIjoxNTg2MjA0ODcyLCJpZGVudGl0eSI6MiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.n_h5_8hQ9F1TY8bFZkb1SzZXogzhORjsSl_BYqS8WnA'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
}

endpoint = URL + 'hoteis'

body = {
    'nome': 'Rio Othon Palace Hotel',
    'estrelas': 4.6,
    'diaria': 385,
    'cidade': 'Rio de Janeiro',
    'site_id': 1
}

resposta = requests.request('POST', endpoint, json=body, headers=headers)

status = resposta.status_code
resp = resposta.json()

print(status)
print(resp)
