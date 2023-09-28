"""
        Cálculo de juros compostos
"""

"""
A é o montante total após o período de tempo t.
P é o principal (ou o valor inicial) investido ou emprestado.
r é a taxa de juros anual (em forma decimal).
n é o número de vezes que os juros são compostos por ano (frequência de capitalização).
t é o número de anos que o dinheiro é investido ou emprestado.
"""

def calcula_juros_compostos(P, r, n, t):
    A = P * (1 + r/n)**(n*t)
    return A

P = float(input("Digite o valor principal (P): "))
r = float(input("Digite a taxa de juros anual (em decimal): "))
n = int(input("Digite o número de vezes que os juros são compostos por ano (n): "))
t = float(input("Digite o número de anos (t): "))

montante_total = calcula_juros_compostos(P, r, n, t)

print(f"O montante total após {t} anos será: R$ {montante_total:.2f}")
