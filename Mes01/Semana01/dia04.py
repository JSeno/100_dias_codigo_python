"""
        Calculadora de IMC
"""
your_weight = float(input('Digite seu peso: '))
your_height = float(input('Digite sua altura em metros: '))
your_imc = your_weight / (your_height * your_height)

print(f'Seu IMC é: {your_imc:.2f}')