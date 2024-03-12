#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7.00 por cada Km acima do limite.

import random
velocidade = random.randrange(0,220)
multa = velocidade*7
if velocidade>80:
    print('Sua velocidade é de {} km/h e você foi multado em R$ {}'.format(velocidade, multa))
else:
    print('Sua velocidade é {} km/h parabéns'.format(velocidade))
print('A multa mínima é {}'.format(81*7))