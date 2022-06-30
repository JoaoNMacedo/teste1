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
            print('Digite uma rota valida...')
            continue





rotaobjeto('rota')
