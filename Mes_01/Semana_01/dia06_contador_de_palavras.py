"""
        Contador de palavras
"""

your_text = str(input("Digite uma frase para que possamos contar quantas palavras ele contem.\n"))
text = your_text.split()
count_text = len(text)
print(f"A quantidade de palavras em seu texto é: {count_text}")