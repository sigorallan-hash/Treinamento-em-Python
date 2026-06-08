# vamos uasr uma variavel chamada nome para
# guardar o nome do cliente, utilizaremos também
# o comando input(in -> dentro | put -> por em algun lugar)

nome = input("Digite o seu nome: ")

print("olá, Sr(a). "+nome)
print(f"olá, Sr(a). {nome}")
# o operador + foi utilizado para concatenar (juntar) o texto entre aspas("") com a variavel nome
print("olá, Sr(a). "+nome+". seja bem vindo")

# abaixo, usamos o comando print com letra a letra 
# f(format) para inserir  uma variavel no meio 
# de uma string. A variavelfoi inserida com chaves (())
# está técnica é chamada de interpolação.

print(f"olá, Sr(a). {nome}. seja bem vindo")