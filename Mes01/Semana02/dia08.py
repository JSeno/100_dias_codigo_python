"""
        Contador de Vogais e Consoantes
"""
def contar_vogais_consoantes(frase):
    vogais = 0
    consoantes = 0

    vogais_lista = "aeiouAEIOU"

    for char in frase:
        if char.isalpha():
            if char in vogais_lista:
                vogais += 1
            else:
                consoantes += 1

    return vogais, consoantes

frase = input("Digite sua frase:\n")
vogais, consoantes = contar_vogais_consoantes(frase)
print("Número de vogais:", vogais)
print("Número de consoantes:", consoantes)