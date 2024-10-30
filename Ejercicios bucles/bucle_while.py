#Juego de adivinar el numero
import random
valor_minimo=int(input("Introduce el valor mínimo: "))
valor_maximo=int(input("INtroduce el valor máximo: "))
secreto=random.randint(valor_minimo,valor_maximo)
numero=int(input(f"A ver si adivinas un numero entero entre {valor_minimo} y {valor_maximo}\nEscribe un numero: "))
intentos=1
while numero != secreto:
    if numero < secreto:
        numero=int(input("¡Demasiado pequeño! Inténtalo de nuevo: "))
    else:
        numero=int(input("¡Demasiado grande! Inténtalo de nuevo: "))
    intentos+=1
print(f"¡Acertaste! Te ha costado {intentos} intentos")
    