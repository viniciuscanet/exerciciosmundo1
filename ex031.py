x = float(input('Qual a distância da viagem em quilometros: '))

if x>200:
    print('A viagem custará R$ {}'.format(x*0.45))
else:
    print('A viagem custará R$ {}'.format(x*0.5))