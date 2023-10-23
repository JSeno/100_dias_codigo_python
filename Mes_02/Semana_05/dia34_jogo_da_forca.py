"""
    Jogo da Forca
"""
import random

palavras_forca = [
    "Abacaxi",
    "Girafa",
    "Computador",
    "Esquilo",
    "Telefone",
    "Montanha",
    "Desenvolvimento",
    "Hipopotamo",
    "Escova",
    "Helicóptero",
    "Guitarra",
    "Oceanografia",
    "Dinossauro",
    "Guarda-chuva",
    "Telescópio",
    "Astronauta",
    "Cachoeira",
    "Elefante",
    "Bicicleta",
    "Xadrez"
]

palavra_secreta = random.choice(palavras_forca)
letras_descobertas = ['_'] * len(palavra_secreta)
tentativas_maximas = 6
tentativas = 0

print("Bem-vindo ao Jogo da Forca!")

while '_' in letras_descobertas and tentativas < tentativas_maximas:
    print("\nPalavra: " + ' '.join(letras_descobertas))
    letra = input("Digite uma letra: ").upper()[0]

    if letra.upper() in palavra_secreta.upper():
        print("Acertou!")
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i].upper() == letra.upper():
                letras_descobertas[i] = letra
    else:
        print("Errou!")
        tentativas += 1

if '_' not in letras_descobertas:
    print("Parabéns, você ganhou! A palavra era:", palavra_secreta)
else:
    print("Você perdeu! A palavra era:", palavra_secreta)
