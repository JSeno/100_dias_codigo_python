"""
        Contador de caracteres na frase
"""
import re 

def remove_caracteres(frase): 
    pattern = re.compile(r'\s+') 
    return re.sub(pattern, '', frase) 

frase = str(input('Digite uma frase:\n '))
frase_contador = len(remove_caracteres(frase))
print(f'O número de caracteres na frase é: {frase_contador}')