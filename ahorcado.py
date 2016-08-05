import funciones
import random
print("Bienvenido a Ahorcado.")
aleatorio = random.randint(0, 150)
palabra_elegida= funciones.palabra(aleatorio)
palabra= list(palabra_elegida)
guiones= []
intento = 0

for i in palabra:
	guiones.append("_ ")

while intento < 7:
	print("")
	print(" ".join(guiones))
	print("")
	letra= input("Ingrese una letra: ")	

	if letra in palabra:
		for i in range(len(palabra)):
			if palabra[i] == letra: 
				guiones[i] = letra
				if palabra == guiones:
					print("")
					print(" ".join(guiones))
					print("")
					print("Felicidades, Ganaste.")
					intento = 7

	else: 
		print("")
		print("Fallaste.")
		print(funciones.muneco(intento))
		intento= intento + 1
		if intento == 7:
			print("Perdiste, la palabra era: " , palabra_elegida)