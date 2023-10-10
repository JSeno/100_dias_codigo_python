"""
        Conversor de Idade para Dias
"""
from rich import print


def conversor_idade_para_dias():
    print('Conversor de Idade para Dias')
    idade = int(input('Digite sua idade: '))
    dias = idade * 365
    print(f'Sua idade em dias é: {dias}')

conversor_idade_para_dias()