import json
import requests

URL = 'http://127.0.0.1:5000/'


token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODYyMDU3MzMsIm5iZiI6MTU4NjIwNTczMywianRpIjoiZDJlNjA5ODAtNzA2Ny00NjM4LWFjYTQtYTVhMmQ2YjM4OGU4IiwiZXhwIjoxNTg2MjA2NjMzLCJpZGVudGl0eSI6MiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.nqItXhH3vW4cQ_DHPwRfgJdyGULOrfu8-rCt_szTXz0'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
}

endpoint = URL + 'hoteis/17'


resposta = requests.request('GET', endpoint, headers=headers)

status = resposta.status_code
resp = resposta.json()

print(status)
print(resp)
