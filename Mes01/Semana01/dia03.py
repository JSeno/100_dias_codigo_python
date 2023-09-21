"""
        Ano bissexto
"""

year = int(input('Digite o ano que você deseja conferir: '))
if year % 4 ==0 and (year%100 != 0 or year%400==0):
    print(f'O ano {year} é bissexto')
else:
    print(f'O ano {year} não é bissexto')