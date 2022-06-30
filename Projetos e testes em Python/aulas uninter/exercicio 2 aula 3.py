print('CALCULADORA DE KWH')

kwh = float(input('Quantos kwh?:'))
tipo =input('Qual o tipo de instalação? (R, C ou I):')

if (tipo =='R'):
    if kwh >= 150:
        preco = 0.7
    else:
        preco = 0.60

elif (tipo == 'C'):
    if kwh >=1000:
        preco = 0.60
    else:
        preco = 0.55

elif(tipo == 'I'):
    if kwh >= 5000:
        preco = 0.60
    else:
        preco = 0.55
else:
    print('Instalação Não Reconhecida!!!')

print('Resultado:{}'.format(preco * kwh))









