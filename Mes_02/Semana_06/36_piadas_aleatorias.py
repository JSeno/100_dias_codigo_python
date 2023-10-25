"""
        Piadas aleatórias
"""

import random

def get_joke():
    jokes = [
        "Por que o programador nunca mente? Porque ele sempre está debugando!",
        "Qual é o animal mais antigo? A zebra, porque está em preto e branco!",
        "Por que os desenvolvedores odeiam a natureza? Porque tem muitos bugs!",
        "Por que o livro de matemática está sempre preocupado? Porque ele tem muitos problemas!",
        "O que o zero falou para o oito?\n Me empresta seu cinto, você está fazendo a minha barriga aparecer!",
        "O que é um círculo? Um quadrado que tomou um Viagra!",
        "Por que o pepino nunca briga? Porque ele é um legume calmo!",
        "O que um pão disse para o outro? 'Vamos amassar!'",
        "Qual é o animal mais antigo? A zebra, porque está em preto e branco!",
        "O que é um vegetariano que come carne? Um ex-vegetariano!",
        "Por que o pato foi à escola? Porque queria melhorar o seu 'quack'!",
        "Como se organiza uma festa do espaço? Você 'planet'!",
        "O que uma impressora diz para outra? Essa folha é sua ou é uma 'impressão'?",
        ]
    return random.choice(jokes)

def main():
    input("Pressione Enter para receber uma piada:")
    joke = get_joke()
    print("\nSua piada do dia:\n", joke)

if __name__ == "__main__":
    main()
