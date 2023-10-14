"""
        Pares de Meias
"""
from rich import print

def sock_pairs(socks):
    sock_list = {}
    for sock in socks:
        sock_list[sock] = sock_list[sock] + 1 if sock in sock_list else 1

    pair_count = 0
    for sock in sock_list:
        pair_count += int(sock_list[sock] / 2)
        
    return pair_count

print(sock_pairs([10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(sock_pairs([1, 2, 1, 2, 1, 3, 2]))
print(sock_pairs([1, 2, 1, 3, 2]))
