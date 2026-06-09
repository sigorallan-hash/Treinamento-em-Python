palavra = input("Digite um texto:  ")
# O comando len(lenght - comptrimento), ou seja,
# conta  a quantidade de caracteres em uma
# coleção
qtd_palavra = len(palavra)
print(qtd_palavra)
cont = 0
while cont <= qtd_palavra:
    print(f"o número é {cont + 1}°, e a letra é {palavra [cont]")
    cont+=1
    