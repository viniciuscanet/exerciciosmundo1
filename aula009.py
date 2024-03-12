nome = 'Vinicius Domingues Canet'
print(nome)

print(nome[0])# Mostra um único caracter

print(nome[0:8])# Mostra entre o primeiro e o caracter na posição 7

print(nome[:8])# Mostra do início até o caracter na posição 7

print(nome[9:])# Mostra do caracter na posição 9 até o final

print(nome[0::4])# Mostra do início até o final, com espaçamentos de 4
print(len(nome)) #Mostra o tamanho/quantidade de caracter

print(nome.count('i')) #Conta quantos 'i' tem na frase

print(nome.count('n', 0, 25)) #Conta quandos 'n' existem entre um intervalo

print(nome.find('i')) #Encontra a posição que começa o 'Can'

print(nome.find('Domingues'))
print(nome.find('domingues')) #ele nao encontra entao o resultado é -1

print('Canet' in nome) #pergunta se tem 'Canet' no nome

print(nome.replace(' Domingues', ''))

print(nome.upper()) #transforma tudo em maiusculo
print(nome.lower()) #transforma tudo em minusculo

print(nome.capitalize()) #Vai deixar todos minusculos menos a primeira letra
print(nome.title()) #Analiza quantas palavras tem e deixa em maiuscula a primeira letra de cada palavra

print(nome.strip()) #remove os espaços vazios e substitui a contagem para o '0' logo na primeira letra
print(nome.rstrip()) #remove os ultimos espaços 'r' de right
print(nome.lstrip()) #remove os primeiros espaços 'l' de left

print(nome.split()) #divide toda a string onde tem espaços, e não mostra os espaços na divisão

print('-'.join(nome)) #junta todas as letras
print('-'.join(nome.split())) #junta as palavras separadas

nomeDividido = nome.strip()
