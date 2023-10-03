"""
        Conversor de Moedas
"""
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('API_KEY')
api_response = requests.get(f"https://api.invertexto.com/v1/currency/USD_BRL?token={api_key}")

if api_response.status_code == 200:
    data = api_response.json()
    usd_brl_data = data.get('BRL_USD', {})
    taxa_cambio = usd_brl_data.get('price')
    print(f'O valor do Dollar é: {taxa_cambio:.2f}')
else:
    print(f"Erro na solicitação. Código de status: {api_response.status_code}")

sua_conversao = float(input('Quanto você gostaria de converter para dolar: '))
conversao = sua_conversao * taxa_cambio
total = print(f'O valor convertido é {conversao:.2f}')
