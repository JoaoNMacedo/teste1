#lista no escopo global para ser utilizada por mais de uma funçao
#a lista vai comportar os dicionarios q por sua vez vão comportar as informaçoes cadastrada.
listaPecas = []
#funções que vão executar o comando do dado de entrada.
def cadastrarPeca(codU):
#dados de entrada e print do codigo unico.
    print('Código da peça: {:0>3}'.format(codU))
    nome = input('Entre com o nome da peça: ')
    fabricante = input('Entre com o fabricante da peça: ')
    valor = float(input('Entre com o valor da peça: '))
#dicionario
    dicionarioPecas = {
                       'código': codU,
                       'nome': nome,
                       'fabricante': fabricante,
                       'valor': valor,}
#função q adiciona os dicionario a lista, criando uma copia do dicionario dentro da lista assim podendo retornar os dicionarios na proxima função
    listaPecas.append(dicionarioPecas.copy())

def consultaPeca():
#essa funcção apresenta um menu tambem
#por isso ela tem um laço e as condiconais q basicamente dizem oq fazer com os dados de entrada assim como no menu do programa princpal.
#cada condicional chama os dicionarios de uma maneira diferente, uma pelo codigo unico, outra pelo fabricante etc...
    while True:
        try:
            op = int(input('1 - Consulta todas as peças.\n'
                           '2 - Consultar peças por código.\n'
                           '3 - Consultar peças por fabricante.\n'
                           '4 - Retornar a menu pricipal'
                           '\n>>>'))

            if op == 1:
                for list in listaPecas:
                    for k, v in list.items():
                        print('---------------------------')
                        print('{} : {}'.format(k, v))

            elif op == 2:
                escolhaCOD = int(input('Digite o código a ser consultado:'))
                for list in listaPecas:
                    if list ['código'] == escolhaCOD:
                        for k, v in list.items():
                            print('{} : {}'.format(k, v))

            elif op == 3:
                fab = input('Digite o o fabricante a ser consultado:')
                for list in listaPecas:
                    if list['fabricante'] == fab:
                        for k, v in list.items():
                            print('---------------------------')
                            print('{} : {}'.format(k, v))

            elif op == 4:
                print('Programa Encerrado...')
                break
            else:
                print('Digite apenas os numeros apresentados no menu...')
        except ValueError:
            print('Digite apenas numeros inteiros...')


#essa função serve para remover um dos dics
def removerPeca():

    remover = int(input('Digite o código da peça a ser removida:'))
    for list in listaPecas:
        if list['código'] == remover:
            listaPecas.remove(list)


#Programa Pricipal.
print('\n+++Controle de estoque JoãoMacedo Bikes+++\n')
#varivel de contagem
codigoUnico = 0
#laço de repetição para o programa se manter em loop até que a condicional decida.
while True:
# try para aceitar apenas oq lhe for imposto e tentar rodar o dado.
    try:
        op = int(input('1 - Cadastrar Peças.\n'
                   '2 - Consultar Peças.\n'
                   '3 - Remover Peças.\n'
                   '4 - sair' 
                    '\n>>>'))
#condicionais q vão determinar oq cada comando deve fazer.
        if op == 1:
            #contador(vai fazer sempre ser 1 a mais começando do 1)
            codigoUnico = codigoUnico + 1
            cadastrarPeca(codigoUnico)
        elif op == 2:
            consultaPeca()
        elif op == 3:
            removerPeca()
        elif op == 4:
            print('Programa Encerrado...')
            break
#se não for um numero do menu... vai rodar o 'else'
        else:
            print('Digite apenas os numeros apresentados no menu...')
 # se o try decidir que oq foi digitado é falso então o except vai rodar.
    except ValueError:
        print('Digite apenas numeros inteiros...')