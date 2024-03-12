#faça um programa que leia os comprimentos dos catetos e calcule a hipotenusa
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

print('O valor da hipotenusa é {}'.format(hypot(co, ca)))
