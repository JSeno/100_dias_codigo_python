"""
    Jogo da Adivinhação
"""

import random


print("+==========================+")
print("Adivinhe qual é o número!")
print("+==========================+")

secret_number = random.randint(1, 50)
your_number = int(input('Digite um número entre 1 e 50: '))

if your_number == secret_number:
    print('Parabéns você acertou')
elif your_number > 50:
    print('Favor escolher um número entre 1 e 50')
elif your_number < 1:
    print('Favor escolher um número entre 1 e 50')
else:
    print("+==============================================================+")
    print(f'Você errou, o número era {secret_number} e você escolheu {your_number}')
    print("+==============================================================+")
