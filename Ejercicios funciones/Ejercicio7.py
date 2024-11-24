def MCD(a,b):
    while a%b!=0:
        c=b
        b=a%b
        a=c
    if a%b==0:
        c=b
    print(f'El MCD es {c}')
numero1=int(input('Numero1: '))
numero2=int(input('Nuemro2: '))
MCD(numero1, numero2)