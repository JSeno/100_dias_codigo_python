"""
    Contador de Espetinhos
"""

from rich import print

def contar_espetinhos(churrasqueira):
    vegetarianos = 0
    nao_vegetarianos = 0

    for linha in churrasqueira:
        for espetinho in linha:
            if espetinho == "-":
                continue
            elif espetinho == "o":
                vegetarianos += 1
            elif espetinho == "x":
                nao_vegetarianos += 1

    return [vegetarianos, nao_vegetarianos]

churrasqueira1 = [
    "--oooo-ooo--",
    "--xx--x--xx--",
    "--o---o--oo--",
    "--xx--x--ox--",
    "--xx--x--ox--"
]

churrasqueira2 = [
    "--oooo-ooo--",
    "--xxxxxxxx--",
    "--o---",
    "-o-----o---x--",
    "--o---o-----"
]

print(contar_espetinhos(churrasqueira1))
print(churrasqueira1)
print(contar_espetinhos(churrasqueira2))
print(churrasqueira2)
