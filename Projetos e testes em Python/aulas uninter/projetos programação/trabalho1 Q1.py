
#Apresentação(cabeçalho)
print('Bem-vindo a Loja do João Macedo')
#Programa principal (com os comandos para execução)
# Dados de entrada! (onde o usuario deposita as informações a seram processadas)
qd = float(input('Quantidade de Produtos:'))
valor = float(input('Valor Unitario:'))
#condiconais, determinam os porques de tudo funcionar como funciona.
if qd >= 0 and qd <= 9:
    p = 0
    vf = qd * valor
    desconto = vf * (p/100)
    dfinal = vf - desconto
    print('Valor sem Desconto:R${:.2f}'.format(vf))
    print('Valor com Desconto:R${:.2f} (ESSA QUANTIDADE NÃO FORNECE DESCONTO...)'.format(dfinal))
elif qd >= 10 and qd <= 99:
    p = 5
    vf = qd * valor
    descbruto = vf * (p/100)
    descfinal = vf - descbruto
    print('Valor sem Desconto:R${:.2f} '.format(vf))
    print('Valor com Desconto:R${:.2f}(5% de desconto)'.format(descfinal))
elif qd >= 100 and qd <= 999:
    p = 10
    vf = qd * valor
    descbruto = vf * (p/100)
    descfinal = vf - descbruto
    print('Valor sem Desconto:R${:.2f}'.format(vf))
    print('Valor com Desconto:R${:.2f}(10% de desconto)'.format(descfinal))
elif qd > 1000:
    p = 15
    vf = qd * valor
    descbruto = vf * (p/100)
    descfinal = vf - descbruto
    print('Valor sem Desconto:R${:.2f}'.format(vf))
    print('Valor com Desconto:R${:.2f}(15% de Desconto).'.format(descfinal))
#caso o numero de entrada for invalido
#o programa é encerrado assim que os resultados são mostrados.







