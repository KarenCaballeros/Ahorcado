import funciones
import random
print("Bienvenido a Ahorcado.")


repetir_jugada = 1	

while repetir_jugada == 1:
	contador_intento = 0
	aleatorio = random.randint(0, 150)
	palabra_elegida= funciones.palabra(aleatorio)
	palabra= list(palabra_elegida)
	guiones= []
	letras_usadas= []
	for i in palabra:
		guiones.append("_ ")
	
	while contador_intento < 7:
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
							contador_intento = 7

			else: 
				print("")
				print("Fallaste.")
				print(funciones.muneco(contador_intento))
				letras_usadas.append(letra)
				contador_intento= contador_intento + 1
				if contador_intento == 7:
					print("Perdiste, la palabra era: " , palabra_elegida)	

	print("")			
	print("Desea...")
	print("1. Jugar de nuevo.")
	print("2. Salir.")			
	repetir_jugada= int(input("Ingrese opcion elegida: " ))					