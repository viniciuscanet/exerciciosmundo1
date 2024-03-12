#crie um programa que leia o nome de uma cidade e dia se ela começa ou não com o nome "santo"

cidade = input('Digite o nome da sua cidade: ').strip()

print('Tem "Santo" no primeiro nome da sua cidade? {}'.format(cidade.split()[0].upper() == 'SANTO'))
