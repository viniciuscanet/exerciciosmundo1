d = float(input('Digite o valor em metros: '))
print('O valor pode ser expresso em {:.3f} cm ou \n'
      '{:.3f} mm.'.format( d*100, d*1000))
