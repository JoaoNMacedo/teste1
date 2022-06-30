#Funções
#Todas as funções possum laços de repetição para caso o usuario digite um dado ivalido, ele repita a entrada.
#condicionais para determinar a parada dos laços e quais são os dados de entrada.
def dimensoesobjeto(altura,largura,comprimento):
    global dimensao
    while True:
        try:
            altura = int(input('Digite a altura (em CM):'))
            largura = int(input('Digite a largura (em CM):'))
            comprimento = int(input('Digite o comprimento (em CM):'))

        except:
            print("Por favor, insira somente números inteiros positivos...")
            continue
        dimensao = altura * largura * comprimento
        if dimensao >= 100000:
            print('Não aceitamos objetos com dimensões tão grandes!')
            continue
        else:
            print('O volume do objeto é (em cm³): {}'.format(dimensao))
            break

def pesoobjeto(pergunta):
    global multPeso
    while True:
        try:
            pergunta = float(input('Digite o peso do objeto (em KG): '))
        except:
            print('Digite um peso valido...')
            print('Entre com o Peso desejado novamente')
            continue
        if pergunta <= 0.1:
            multPeso = 1
        elif pergunta >= 0.11 <= 1:
            multPeso = 1.5
        elif pergunta >= 1.1 <= 10:
            multPeso = 2
        elif pergunta >= 10.1 <= 30:
            multPeso = 3
        if pergunta >= 30:
            print('Não aceitamos objetos tão pesados')
            print('Entre com o Peso desejado novamente...')
            continue
        else:
            break

def rotaobjeto(rota):
    global multRota
    while True:
        print('Selecione a Rota:')
        print('RS - De Rio de Janeiro até São Paulo	')
        print('SR - De São Paulo até Rio de Janeiro')
        print('BS - De Brasília até São Paulo')
        print('SB - De São Paulo até Brasília')
        print('BR - De Brasília até Rio de Janeiro')
        print('RB - Rio de Janeiro até Brasília	')
        rota = input('>>>')
        if rota.upper() == 'RS':
            multRota = 1
            break
        elif rota.upper() == 'SR':
            multRota = 1
            break
        elif rota.upper() == 'BS':
            multRota = 1.1
            break
        elif rota.upper() == 'SB':
            multRota = 1.2
            break
        elif rota.upper() == 'BR':
            multRota = 1.5
            break
        elif rota.upper() == 'RB':
            multRota = 1.5
            break
        else:
            print('Você digitou uma rota que não existe')
            print('Digite uma rota valida...')
            continue
#variaveis que foram globalizadas la nas funções pra poderem entregar um resultado no programa principal.
dimensao = 0
multRota = 0
multPeso = 0
#Programa Pricipal
#cabeçalho e funçoes na ordem correta.
print('\nBem-vindo a João Macedo Transportes ltda.')
#as funções sendo empregadas no progama principal.
dimensoesobjeto('Digite a altura', 'Digite a Largura', 'Digite o comprimento')
pesoobjeto('Peso do objeto')
rotaobjeto('rota')
#calculo para somar o total do valor.
total = dimensao*multRota*multPeso
print('Total a pagar(R$):{:.2f} (Dimensão= {}, Rota = {}, Peso= {}).'.format(total, dimensao, multRota, multPeso))
#Saída ou resultado do programa.




