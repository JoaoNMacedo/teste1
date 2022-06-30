palavras = {'Mario', 'Luigi', 'Peach', 'Yoshi', 'Browser'}
for palavra in palavras:
  print('\nPalavra: {}.Vogais:'.format(palavra.upper()), end='')
  for letra in palavra:
       if letra.lower() in'aeiou':
            print(letra.upper(), end=' ')
