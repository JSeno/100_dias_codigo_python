"""
        Próximo Primo
"""

def is_prime(number):
    if (number < 2):
        return False
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
    return True


def next_prime(number):
    number = int(number)
    return number if is_prime(number) else next_prime(number + 1)

print(next_prime(8))
print(next_prime(12))
print(next_prime(123))