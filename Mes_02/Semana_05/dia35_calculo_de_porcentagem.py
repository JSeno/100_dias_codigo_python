"""
        Cálculo de Porcentagem
"""

valor = float(input("Digite o valor R$: "))
porcentagem = float(input("Digite a porcentagem: "))

calculo = valor * (porcentagem / 100)
print(f'{porcentagem}% de {valor} = R$ {calculo:.2f}')
