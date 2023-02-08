#Aquesta funció mostra per pantalla indicant el número més gran i el més petit
#Si els dos números són iguals no es mostren per pantalla
def granPetit(num1, num2):
    if num1 > num2:
        print('El número {num1} és més gran que el número {num2}.'.format(num1=num1, num2=num2))
    elif num1 < num2:
        print('El número {num2} és més gran que el número {num1}.'.format(num1=num1, num2=num2))