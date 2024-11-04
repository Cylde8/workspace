#programa que pide un numero y calcula el factorial
numero=int(input('Dime un número: '))
factorial=1
for i in range(1,numero+1):
    factorial*=i
print(f'El factorial de {numero} es: {factorial}')
