"""
        Busca cep via API
"""

import requests
from rich import print

cep = input('Digite o CEP: ')

busca_cep = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
# print (busca_cep.json())
data = busca_cep.json()
print('+============================+')
print(f'CEP: {data["cep"]}')
print(f'Logradouro: {data["logradouro"]}')
print(f'Bairro: {data["bairro"]}')
print(f'Cidade: {data["localidade"]}')
print(f'Estado: {data["uf"]}')
print('+============================+')