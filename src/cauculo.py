cpf_original = input(" Digite seu cpf original, apenas números:  ")
# Ajuda a contar os números de cpf no laço while
i = 0
# Guardar os 9 primeiros digitos do cpf
cpf_9 = ""

# Enquanto (while) o valor de 1 for menor que 9, neste caso, irá até 9  
# vai pegando um número por vez  no cpf_original (digitado pelo usuário com 11 digitos) 
# e vai adicionado, um ao lado do outro, na variavel cpf_9 a ideia  é obter os 9 digitos do cpf.

while i < 9:
    cpf_9 += cpf_original[i]
    i+= 1

print(cpf_9)
peso = 10
resultado = 0

i = 0
while i < 9:
    resultado += int(cpf_9[i]) * peso
    peso-=1
    i+=1
print(resultado)
resto = resultado % 11
if resto < 2:
    cpf_9 += "0"
else:
    cpf_9 += str(11-resto)
    
print(cpf_9)
# para caucular o primeiro digito verificador, irmos usar  cada número do  
# cpf_9 multiplicação pelo peso que vai de 10 a 2

# outro código
peso = 10
resultado = 0
# 
# Avariavel resta guarda o resultado do cauculo entre o resultado, que
# foi obtido dentro do laço while com o número 11, nesta operação estamos
# obtendo o resto da divisão, por isto, usamos o operador %
# se o resto da divisão  for menor que 2, então o primeiro digito
# verificador  
#  
i2 = 0
while i2 < 9:
    resultado += int(cpf_9[i2]) * peso
    peso-=1
    i2+=1
print(resultado)
resto = resultado % 11
if resto < 2:
    cpf_9 += "0"
else:
    cpf_9 += str(11-resto)
    
print(cpf_9)