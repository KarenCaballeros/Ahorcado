import funciones
import random
print("Bienvenido a Ahorcado.")
aleatorio = random.randint(0, 150)
palabra_elegida= funciones.palabra(aleatorio)
palabra= list(palabra_elegida)
guiones= []
intento = 0
letras_usadas= []

for i in palabra:
	guiones.append("_ ")

repetir_jugada = 1	

while repetir_jugada == 1:
	while intento < 7:
		print("")
		print(" ".join(guiones))
		print("")
		letra= input("Ingrese una letra: ")
		if letra in letras_usadas:
			print("Ya has usado esta letra, ingresa otra!")
		else:		
			if letra in palabra:
				for i in range(len(palabra)):
					if palabra[i] == letra: 
						guiones[i] = letra
						letras_usadas.append(letra)
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
				letras_usadas.append(letra)
				intento= intento + 1
				if intento == 7:
					print("Perdiste, la palabra era: " , palabra_elegida)	

	print("")			
	print("Desea...")
	print("1. Jugar de nuevo.")
	print("2. Salir.")			
	repetir_jugada= int(input("Ingrese opcion elegida: " ))					