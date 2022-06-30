#Assim voce cria uma função

def valida_int(pergunta,min,max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def borda(s1):
    tam = len (s1)

    if tam:
        print('+','-'* tam,'+')
        print('|',s1,'|')
        print('+','-'* tam,'+')

borda('enzo fedido demais slk')


def validastring(x,y):
    res = x+y
    print(res)



#trabalho q3
if rota.upper() != 'rs' or rota.upper() != 'sr' or rota.upper() != 'bs' or rota.upper() != 'sb' or rota.upper() != 'br' or rota.upper() != 'rb':
    print('digite uma rota valida')
    continue

    cadastro = {'codigo': [], 'nome': [], 'fabricante': [], 'valor': []}
    cadastro['codigo'].append(codP)
    cadastro['nome'].append(nome)
    cadastro['fabricante'].append(fab)
    cadastro['valor'].append(preco)



def cadastrarPeca(nomepeca, fabricante, valor):
    global cadGeral,cadUni
    codAP = 1
    codP = 0
    cadGeral = {}
    cadUni = []
    while True:
        print('Código da Peça: {:0>3}'.format(codAP))
        codAP += 1
        codP += 1
        cadGeral['codigo'] = codP
        cadGeral['nome'] = input(nomepeca)
        cadGeral['fabricação'] = input(fabricante)
        cadGeral['valor'] = input(valor)
        cadUni.append(cadGeral.copy())



      if op == 1:
            for i in cadUni:
                for c, d in i.items():
                    print('{} : {}'.format(c, d))





