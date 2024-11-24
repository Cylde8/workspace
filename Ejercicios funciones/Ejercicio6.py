def Login(a,b):
    intentos = 1 
    while a!='usuario1' or b!='asdasd':
        print('Error')
        if intentos < 3:
            a=input('Usuario: ')
            b=input('Contraseña: ')
        else:
            print('Has superado el límite de intentos')
            break
        intentos+=1
    if a=='usuario1' and b=='asdasd':
        print('Verdadero')

usuario=input('Usuario: ')
contraseña=input('Contraseña: ')

if usuario=='usuario1' and contraseña=='asdasd':
    print('Verdadero')
else:
    Login(usuario,contraseña)