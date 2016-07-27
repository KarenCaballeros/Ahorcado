import funciones
import random
print("Bienvenido")
num = random.randint(0, 99)
palabra= funciones.palabra(num)
espacios= (len(palabra) * "_ ")
print(espacios)

letra= input("Ingrese una letra: ")	

for i in palabra:
	if i == letra:
		espacios=  

