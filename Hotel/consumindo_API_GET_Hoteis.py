import json
import requests

# consumindo GET /hoteis http://127.0.0.1:5000/

URL = 'http://127.0.0.1:5000/'

resposta_hoteis = requests.request('GET', URL + 'hoteis')

hoteis = resposta_hoteis.json()

tamanho = len(hoteis['hoteis'])

hotel = hoteis['hoteis'][0]

print(resposta_hoteis.status_code)

print(resposta_hoteis.json())

print(tamanho)

print(hotel)


lista_hoteis = hoteis['hoteis']

for hotel in lista_hoteis:
    # k = hotel['nome']
    print(hotel['nome'])

# API do Mercado livre

URL_livre = 'https://api.mercadolibre.com/sites'

lista_site = requests.request('GET', URL_livre)


lista = lista_site.json()

print(lista)
