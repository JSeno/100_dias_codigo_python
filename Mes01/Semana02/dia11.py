"""
        Média de Notas
"""

def calc_media_nota():
    nota_1 = float(input("Digite a a primeira nota: "))
    nota_2 = float(input("Digite a a segunda nota: "))
    nota_3 = float(input("Digite a a terceira nota: "))
    nota_4 = float(input("Digite a a quarta nota: "))

    resultado = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    print(f'A média total de notas é: {resultado}')

calc_media_nota()
