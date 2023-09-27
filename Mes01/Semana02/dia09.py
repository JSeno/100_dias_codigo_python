"""
        Verificado de Palíndromo
"""

def verficador_palindromo(texto):
    texto = texto.replace(" ", "").lower()

    return texto == texto[::-1]

seu_texto = str(input("Digite seu texto:\n"))

if verficador_palindromo(seu_texto):
    print(f"Seu texto {seu_texto} é palíndromo")
else:
    print(f"Seu texto {seu_texto} não é um palíndromo")
