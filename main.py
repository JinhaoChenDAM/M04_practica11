# Importem els altres arxius.
import exercici1_A as e1a
import exercici2_A as e2a
import exercici3_A as e3a
import exercici1_B as ex1
import exercici2_B as ex2
import exercici3_B as ex3

# Cridar funcion de exercici 1A
e1a.compareNum(2, 2)
e1a.compareNum(2, 3)
e1a.compareNum(2, 1)

# Cridar funcion de exercici 2A
e2a.names()

# Cridar funcion de exercici 3A
e3a.guessFrom0to100()

# Demanem escriure dos números per consola i iniciem el métode granPetit del arxiu exercici1_B
print("Escriu un número")
num1 = input()
print("Escriu un altre número")
num2 = input()
print(ex1.granPetit(num1, num2))

# Demanem escriure un número per consola i iniciem el métode parellSenar del arxiu exercici2_B
print("Escriu un número per saber si és par o senar:")
num3 = input()
print(ex2.parellSenar(int(num3)))

# Demanem escriure la nostre edat i el nostre sou per consola i iniciem el métode anemAHisenda del arxiu exercici3_B
print("Introdueix la teva edat:")
edat = input()
print("Introdueix el teu sou:")
ingresos = input()
print(ex3.anemAHisenda(int(edat), int(ingresos)))