#crie um programa que leia um número inteiro e mostre na tela se ele é par ou inpar

x = int(input('Digite um valor inteiro qualquer: '))

if x % 2==0:
    print('O número {} é par'.format(x))
else:
    print('O número {} é ímpar'.format(x))
