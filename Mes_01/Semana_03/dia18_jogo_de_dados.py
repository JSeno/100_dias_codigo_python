"""
    Jogo de dados de 6 lados
"""

import random

def rolar_dado():
    resposta = input("Vamos jogar um jogo de dados? (S) Sim ou (N) Não: ")
    if resposta.lower() == "s":
        valor = random.randint(1, 6)
        print(f"O valor do dado foi {valor}")

    else:
        print("Obrigado por jogar!")

rolar_dado()
