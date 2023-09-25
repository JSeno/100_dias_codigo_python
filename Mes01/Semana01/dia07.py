import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["@", "!", "#", "$", "%", "&", "*"]

num_chars = int(input('Digite quantos caracteres você deseja em sua senha: '))

if num_chars <= 0:
    print("Escolha inválida.")
else:
    all_chars = letters + numbers + symbols
    
    password = ""
    
    for _ in range(num_chars):
        char = random.choice(all_chars)
        password += char
    
    print("Senha gerada:", password)
