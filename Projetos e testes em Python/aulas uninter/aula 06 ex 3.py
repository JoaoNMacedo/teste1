cadastro = {'nome':[],'ano':[], 'sexo':[]}

while True:
    terminar = input('Deseja Casdastrar Uma Pessoa? [S/N] ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO...')
        continue

    nome = input('Qual seu nome?: ')
    ano = input('Qual seu ano de nascimento?: ')
    sexo = input('Qual seu sexo? [M/F]: ')

    cadastro['nome'].append(nome)
    cadastro['ano'].append(ano)
    cadastro['sexo'].append(sexo.upper())

print(cadastro)
