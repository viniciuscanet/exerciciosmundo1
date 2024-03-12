n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))
n3 = float(input('digite o terceiro numero: '))

if n1>n2:
    if n1>n3:
        print('O maior número é o {}'.format(n1))
        if n2>n3:
            print('O menor número é {}'.format(n3))
        else:
            print('O menor número é {}'.format(n2))
    else:
        print('O maior número é o {}'.format(n3))
        print('O menor número é o {}'.format(n2))
else:
    if n2>n3:
        print('O maior número é o {}'.format(n2))
        if n1>n3:
            print('O menor número é {}'.format(n3))
        else:
            print('O menor número é {}'.format(n1))
    else:
        print('O maior número é o {}'.format(n3))
        print('O menor número é o {}'.format(n1))
