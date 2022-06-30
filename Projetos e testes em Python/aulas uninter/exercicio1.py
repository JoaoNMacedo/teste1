preco = float(input('Digite o Preço do Produto:'))
p = float(input('Digite o Percentual de desconto(0-100)%:'))

desconto = preco * (p/100)
final= preco - desconto

print('o preço do produto é {}.' ' Desconto sera de {}.'.format(preco, p))
print('valor calculado de desconto: {}. valor final do produto {}'.format(desconto, final))



