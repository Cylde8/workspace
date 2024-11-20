def max_de_tres(a,b,c):
    if a>b:
        if a>c:
            mayor=a
        else:
            mayor=c
    else:
        if b>c:
            mayor=b
        else:
            mayor=c
    return mayor

numero1=int(input('Introduzca el primer número: '))
numero2=int(input('Introduzca el segundo número: '))
numero3=int(input('introduzca el tercer número: ' ))
maximo=max_de_tres(numero1,numero2, numero3)
print(f'El máximo es:{maximo} ')
