# Aquesta funció mostra per pantalla si el número és parell o senar
def parellSenar(num1):
    if num1 % 2 == 0:
        print('El número {num1} és parell.'.format(num1=num1))
    else:
        print('El número {num1} és senar'.format(num1=num1))