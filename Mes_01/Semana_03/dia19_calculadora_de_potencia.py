"""
    Calculadora de Potência
"""
def calculadora_potencia():
    base = int(input('Digite o valor da base: '))
    expoente = int(input('Digite o valor do expoente: '))
    potencia = base ** expoente
    print(f'A potência de {base} elevado a {expoente} é igual a {potencia}')



calculadora_potencia()