def valida_int(pergunta,min,max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existeArq(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do Arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))

def cadastrarJogo(nomeArquivo, nomeJogo, videoGame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir arquivo')
    else:
        a.write('{}    |   {}\n'.format(nomeJogo, videoGame))

def borda(s1):
    tam = len (s1)

    if tam:
        print('-','-'* tam,'-')
        print('|',s1,'|')
        print('-','-'* tam,'-')

#Progama Principal
arquivo = 'games.txt'
if existeArq(arquivo):
    print('Arquivo Localizado no computador')
else:
    print('Arquivo Inexistente')
    criaArquivo(arquivo)
while True:
    borda('              ''MENU''                 ')

    print('1-Cadastrar Novo Item ')
    print('2-Listar Cadastro ')
    print('3-Sair ')

    op = valida_int('Escolha a opção desejada:',1,3)

    if op == 1:
        print('Opcão Cadastrar Novo Item...\n')
        nomeJogo = input('Nome do Jogo: ')
        videoGame = input('Nome do videoGame: ')
        cadastrarJogo(arquivo, nomeJogo, videoGame)
    elif op == 2:
        print('Listagem de itens já cadastrados...\n')
        listarArquivo(arquivo)

    elif op == 3:
        print('Encerrando programa...')
        break