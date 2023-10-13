"""
        Johny fez progresso
"""
from rich import print


def progress_johnny(km_corrida):
    dias_progresso = 0
    for i in range(1, len(km_corrida)):
        if km_corrida[i] > km_corrida[i-1]:
            dias_progresso += 1
    return dias_progresso

print(progress_johnny([3, 4, 5, 1, 2]))
print(progress_johnny([1, 2, 3, 4, 5]))
print(progress_johnny([4, 2, 5, 7, 0]))