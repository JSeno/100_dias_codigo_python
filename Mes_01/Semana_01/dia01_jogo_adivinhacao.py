"""
    Jogo da Adivinhação
"""

import random

def jogo_adivinhacao(your_number):
    print("+==========================+")
    print("Adivinhe qual é o número!")
    print("+==========================+")

    secret_number = random.randint(1, 50)

    if your_number == secret_number:
        return 'Parabéns você acertou'
    elif your_number > 50 or your_number < 1:
        return 'Favor escolher um número entre 1 e 50'
    else:
        return f'Você errou, o número era {secret_number} e você escolheu {your_number}'
