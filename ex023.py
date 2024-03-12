#faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

num = str(input('Digite um númetro entre 0 e 9999 utilizando 4 digitos: '))

print('O número que você digitou foi: {}'.format(num))


uni = num[len(num)-1]
dez = num[len(num)-2]
cen = num[len(num)-3]
mil = num[len(num)-4]

print('Unidade é: {}\n'
      'Dezena é: {}\n'
      'Centena é: {}\n'
      'Milhar é: {}'.format(uni, dez, cen, mil))