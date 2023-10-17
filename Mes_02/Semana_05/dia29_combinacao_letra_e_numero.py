"""
        Letra e número
"""


def letra_combinacao(digitos):
    digitos_letra = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    combinacoes = ['']

    for digito in digitos:
        letras = digitos_letra.get(digito, '')
        combinacoes = [prefixo + letra for prefixo in combinacoes for letra in letras]

    return combinacoes

print(letra_combinacao('234'))


