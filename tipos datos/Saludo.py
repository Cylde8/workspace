MAX_SALUDOS=5
num_saludos=0
quieres_saludar = 'S'
while quieres_saludar == 'S':
    print('Hola qué tal!')
    num_saludos+=1
    if num_saludos==MAX_SALUDOS:
        print('Has alcanzado el máximo de saludos')
        break    
    quieres_saludar = input('¿Quieres otro saludo? [S/N] ')
    while quieres_saludar not in ('S','N'):
        quieres_saludar=input('Respuesta invalida\n¿Quieres otro saludo? [S/N] ')
      
print('Que tengas un buen día')