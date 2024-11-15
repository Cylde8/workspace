def minimo(a,b):
    if a<b:
        print(f'el numero minimo entre {a} y {b} es {a}')
    elif a>b:
        print(f'el numero minimo entre {a} y {b} es {b}')
    else:
        print('Los números son iguales')
numero1=int(input('Introduce el número 1: '))
numero2=int(input('Introduce el número 2: '))
minimo(numero1,numero2)