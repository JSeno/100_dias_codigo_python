"""
        Verificador de números impares
"""

num = int(input("Digite um número: "))
verifica = num % 2
if verifica != 0:
    print(f"O número {num} é ímpar")
else:
    print(f"O número {num} é par")
