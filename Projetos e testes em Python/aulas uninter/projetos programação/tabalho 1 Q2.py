def borda(s1):
    tam = len (s1)

    if tam:
        print('-','-'* tam,'-')
        print('|',s1,'|')
        print('-','-'* tam,'-')
#cabeçalho
print ('Bem-vindo a Lanchonete João Macedo')
borda('                  *Cardapio*                  ')
#Informações para visualiazção do cliente.
print ('    | Código |       Descrição     |  Valor  |')
print ('    |  100   |   Cachorro-Quente   |  9.00   |')
print ('    |  101   |Cachorro-Quente Duplo|  11.00  |')
print ('    |  102   |        X-Egg        |  12.00  |')
print ('    |  103   |        X-salada     |  13.00  |')
print ('    |  104   |        X-bacon      |  14.00  |')
print ('    |  105   |        X-Tudo       |  17.00  |')
print ('    |  200   |  Refrigerante Lata  |   5.00  |')
print ('    |  201   |     Chá Gelado      |   4.00  |')
#programa principal
dinheiro = 0
valor = 0
#Laço de Repetição bota o programa em looping, até q algumas das condicionais digam o contrario.
while True:
    cod = input('Digite o Codigo do produto desejado:')
    cod = int(cod)
#condicionais, dizem ao programa como empregar os dados de entrada
    if cod == 100 or cod == 101 or cod == 102 or cod == 103 or cod == 104 or cod == 105 or cod == 200 or cod == 201:
        if cod == 100:
            valor = 9
            print('Você Pediu Um Cachorro Quente no valor de R$ 9,00')
        elif cod == 101:
            valor = 11
            print('Você Pediu Um Cachorro Quente  duplo no valor de R${:.2f}'.format(valor))
        elif cod == 102:
            valor = 12
            print('Você Pediu Um X-Egg de R$ 12,00')
        elif cod == 103:
            valor = 13
            print('Você Pediu Um X-Salada no valor de R${:.2f}'.format(valor))
        elif cod == 104:
            valor = 14
            print('Você Pediu Um X-Bacon no valor de R${:.2f}'.format(valor))
        elif cod == 105:
            valor = 17
            print('Você Pediu Um X-Tudo no valor de R${:.2f}'.format(valor))
        elif cod == 200:
            valor = 5
            print('Você Pediu Um Refrigerante Lata no valor de R${:.2f}'.format(valor))
        elif cod == 201:
            valor = 4
            print('Você Pediu Um Chá Gelado no valor de R${:.2f}'.format(valor))

        print('Deseja pedir mais alguma coisa?')
        print('1 - SIM')
        print('2 - NÂO')
        son = int(input('>>>>'))
        dinheiro += valor
#condicional que diz quando o programa deve encerrar
        if son == 2:
            print('Valor total a ser pago: R${:.2f}'.format(dinheiro))
            break
#essa condicional diz q se a condicional de cima nao for a verdadeira, então o programa deve continuar
        else:
            continue
#caso a pessoa coloque um codigo de entrada invalido a saida do programa sera essa
    else:
        print('Opcção Invalida...')
































