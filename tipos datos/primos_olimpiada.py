#Programa que decide si un numero es primo o no y que calcula un numero de primos consecutivos
t=int(input('Indica el numero de casos que hse deben procesar: '))
for i in range(0,t):
    k=int(input('Introduce un numero entre 0 y 100: '))
    n=int(input('Introduce un número entero entre 1 y 1000: '))
    if k==0:
        if n%2==0:
            print('NO')
        else:
            print('SI')