import funciones
import random
print("Bienvenido!")
lista_variables= []
num = random.randint(0, 99)
print(len(funciones.palabra(num)) * "_ ")

munequito= [" _________" , " |        |" , " |" , " |" , " |" , "_|_"]

for i in munequito:
 	print(i)

 letra= input("Ingrese una letra: ")	