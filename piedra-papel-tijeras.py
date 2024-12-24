# Se puede mejorar el nombre en la segunda solicitud
# Lo ingresado por el usuario sea lowerCase  de tal forma  de comparar  minúsculas 
# Más de un turno con el bucle while  


nombre1 = input("¿Como se llamará el jugador 1?: ")
nombre2 = input("¿Como se llamará el jugador 2?: ")

jugador1 = input("Hola jugador 1! ¿Qué elijes? ¿Piedra, papel o tijeras?: ")
jugador2 = input("Hola jugador 2! ¿Qué elijes? ¿Piedra, papel o tijeras?: ")

#Metodo de refactorizacion punto (B)
condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1 == jugador2:     #a refactorizar (A)
    print("¡Ha sido un  empate!")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado:", nombre1)
else:
    print("Ha ganado:", nombre2)
