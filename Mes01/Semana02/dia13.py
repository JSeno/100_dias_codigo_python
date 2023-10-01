"""
        Gerador de Tabuadas
"""
tabuada=int(input("Qual tabuada você gostaria de ver: "))
print(f"Então vamos ver a tabuada do número: {tabuada}")
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )