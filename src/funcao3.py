#importar funções específicas de um módulos,
#o comando from(origem) que indica de onde vem as funções,
#ou seja, de qual módulo, está extraindo as funções.
#o comando import indica quais funções você irá usar do(from)
#modúlo carregado pelo comando from(origem).

from os import system, cpu_count, getenv
from math import sqrt, pow, pi

system('cls')
print('=============== ORIGEM OS ===============')
print(cpu_count())
###print(getenv())
print('=============== ORIGEM MATH ===============')
print(sqrt(49))
print(pow(2,5))