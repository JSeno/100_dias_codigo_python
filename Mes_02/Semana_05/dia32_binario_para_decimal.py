"""
        Binário para Decimal
"""

def bin_to_dec(binary_str):
    decimal = 0
    n = len(binary_str)

    for i in range(n):
        digit = int(binary_str[i])
        decimal += digit * (2 ** (n - 1 - i))

    return decimal

binary_input = input("Insira um número binário: ")

if not all(digit in ['0', '1'] for digit in binary_input):
    raise ValueError("A entrada deve conter apenas 0s e 1s")
else:
    decimal_output = bin_to_dec(binary_input)

print(f"O equivalente decimal de {binary_input} é {decimal_output}")
