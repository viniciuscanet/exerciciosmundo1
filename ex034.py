salario = float(input('Digite o valor do seu salário: '))

salario10 = salario*1.1

salario15 = salario*1.15

if salario>1250:
    print('Seu novo salário é de R$ {:.2f}'.format(salario10))
else:
    print('Seu novo salário é de R$ {:.2f}'.format(salario15))
