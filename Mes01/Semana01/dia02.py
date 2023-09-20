"""
        Calculadora simples
"""

num1 = int(input('Digite seu primeiro número: '))
num2 = int(input('Digite seu segundo número: '))
print('Qual tipo de operação você deseja fazer: ')
oper = int(input('Soma (1), Subtração (2), Multiplicação (3), Divisão (4):' ))

if oper == 1:
    res = num1 + num2
    print(f'A soma de {num1} e {num2} é {res}')

elif oper == 2:
    res = num1 - num2
    print(f'A subtração de {num1} e {num2} é {res}')

elif oper == 3:
    res = num1 * num2
    print(f'A multiplicação de {num1} e {num2} é {res}')

elif oper == 4:
    res = num1 / num2
    print(f'A divisão de {num1} e {num2} é {res}')

else:
    print('Operação inválida')