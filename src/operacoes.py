num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

# para realizar as operações, será 
# nessesário converter as variaveis em int(inteiros) entre 
# num1 e num2 em tipos númericos, podendo ser: int ou float

num1 = int(num1)
num2 = int(num2)

soma = num1 + num2
subtrair = num1 - num2
multiplicar = num1 * num2
dividir = num1 / num2

print(f"a soma entre números {num1} e {num2} é {soma}")
print(f"a soma entre números {num1} e {num2} é {subtrair}")
print(f"a soma entre números {num1} e {num2} é {multiplicar}")
print(f"a soma entre números {num1} e {num2} é {dividir}")
