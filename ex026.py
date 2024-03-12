#Faça um programa que leia a frase pelo teclado e mostre:
frase = input('Digite qualquer frase: ')
frase = frase.lower()
print('Aparece a letra "a" na frase {} vezes'.format(frase.count('a')))

print('A posição que a primeira letra "a" aparece é: {}'.format(frase.find('a')))

print('A posição que a primeira letra "a" aparece é: {}'.format(frase.rfind('a')))

