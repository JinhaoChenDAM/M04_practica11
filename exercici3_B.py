#Aquesta funció mostra per pantalla si has de declarar a hisenda
def anemAHisenda (edat, ingresos):
    if edat>=18 and ingresos>1200:
        print('És necessari que facis la declaració d’hisenda ja que tens {edat} anys i cobres'
            ' més de 1200 euros.'.format(edat=edat))
    elif edat < 18:
        print('Encara no pots fer la declaració ja que tens {edat} '
              'anys i no ets major de 18'.format(edat=edat))
    else:
        print('Encara no pots fer la declaració ja que no cobres més de 1200 euros.')
