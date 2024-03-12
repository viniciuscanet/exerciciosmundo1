from math import sin, cos, tan, radians

x = float(input('Digite o ângulo em : '))
print('Portanto o seno = {:.3},\n'
      'o cosseno = {:.3},\n'
      'e a tangente = {:.3}.'.format(sin(radians(x)), cos(radians(x)), tan(radians(x))))

