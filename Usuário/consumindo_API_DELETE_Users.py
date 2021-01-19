import json
import requests

URL = 'http://127.0.0.1:5000/'

endpoint = URL + 'usuarios/1'

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODYyODQwNTQsIm5iZiI6MTU4NjI4NDA1NCwianRpIjoiNjg0ZDk0ODEtNDNmYy00YmQ4LThmYjgtNDU5MmE3YmNjNDI3IiwiZXhwIjoxNTg2Mjg0OTU0LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.axvUNyTOc7MR33dGv9Jv__9QUMdu4cm8M_LXi6-IQKM"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
}

resposta = requests.request('DELETE', endpoint, headers=headers)

status = resposta.status_code
resp = resposta.json()

print(status)
print(resp)
