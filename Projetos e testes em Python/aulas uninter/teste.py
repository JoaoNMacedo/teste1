print('Calculadora')
print('Escolha a operação')
print('+  -  / *')



while True:
    op = input('Digite a operação desejada:')
    if op == '+' or op == '-' or op == '/' or op == '*':
        x = float(input('Digite o 1° Valor a calcular:'))
        y = float(input('Digite o 2° valor a calcular:'))

    if (op == '+'):
        res = x + y
        print('Resultado {} + {} = {}'.format(x,y,res))
        continue
    elif (op == '-'):
        res = x - y
        print('Resultado {} - {} = {}'.format(x,y,res))
        continue
    elif (op == '/'):
        res = x / y
        print('Resultado {} / {} = {}'.format(x,y,res))
        continue
    elif (op == '*'):
        res = x * y
        print('Resultado {} * {} = {}'.format(x,y,res))
        continue
    elif op == 'sair':
        break

    else:
        print('')
        print('Operação Invalida')
        print('')



print('ENCERRANDO PROGRAMA!!!!')




