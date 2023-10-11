"""
        Procurando Nemo
"""

Nemo = "Nemo"

def find_nemo():
    text = str(input("Digite sua frase para fazer a procura de onde ele está:\n"))
    text_split = text.split()
    print(text_split)
    
    return print("O nemo está na posição: {}".format(text_split.index(Nemo) + 1))


find_nemo()