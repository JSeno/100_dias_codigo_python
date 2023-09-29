"""
        Cálculo de juros compostos
"""

def calc_juros_compostos():
    capital = float(input("Digite o valor Capital: "))
    taxa_juros = float(input("Digite a taxa de juros anual (em decimal): "))
    juros_ano = int(input("Digite o número de vezes que os juros são compostos por ano: "))
    tempo = float(input("Digite o número de anos: "))
    
    montante = capital * (1 + taxa_juros / juros_ano)**(juros_ano * tempo)
    return montante

def calc_juros_simples():
    capital = float(input("Qual é o valor do capital? "))
    taxa_juros = float(input("Qual é o valor da taxa de juros? ")) / 100
    tempo = int(input("Duração de tempo (em anos): "))
    
    montante = capital + (capital * taxa_juros * tempo)

    return montante

choice = input("Você gostaria de calcular juros simples (S) ou compostos (C):\n").lower()
if choice == "s":
    print("Você escolheu juros simples\n")
    montante = calc_juros_simples()
    print(f"O montante total é: R$ {montante:.2f}")
elif choice == "c":
    print("Você escolheu juros compostos\n")
    montante = calc_juros_compostos()
    print(f"O montante total é: R$ {montante:.2f}")
else:
    print('Escolha inválida')

