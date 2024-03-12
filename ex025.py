#crie um programa que leia o nome de uma pessoa
# e diga se ela começa ou não com o nome "Silva"

nome = input('Digite o nome da pessoa: ')
nome = nome.upper()

print('O nome dessa pessoa tem "Silva"? {}'.format('SILVA' in nome))