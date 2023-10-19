"""
        Busca Binária  
"""

def num_trees(n):
    dp = [0] * (n + 1)
    
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]

    return dp[n]

n = int(input(f'Insira um número: '))
resultado = num_trees(n)
print(resultado)
