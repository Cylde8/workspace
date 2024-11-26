def MCD(a,b):
    while a%b!=0:
        a,b=b,a%b
    print(f'El MCD es {b}')
numero1=int(input('Numero1: '))
numero2=int(input('Nuemro2: '))
MCD(numero1, numero2)