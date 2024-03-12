import random
x = int(input('Digite um número inteiro entre 0 e 10:' ))
y = int(random.randrange(11))

if x==y:
    print('Parabens, você venceu!!!')
else:
    print('Parabéns, você perdeu!!!')
print('O número que o computador escolheu foi {}'.format(y))