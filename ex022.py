#crie um programa que leia o nome completo de uma pessoa e mostr:

nome = input('Digite seu nome: ')

print('Seu nome com todas as letras maiusculas é: {}'.format(nome.upper()))

print('Seu nome com todas as letras minusculas é: {}'.format(nome.lower()))

nv = int(len(nome))
ne = int(nome.count(' '))

print('A quantidade de letras no seu nome é: {}'.format(nv-ne))

primeiroNome = nome.split()[0]
print(len(primeiroNome))
