#Ejercicio que muestra el valor de la clave história
diccionario={'clase':{
    'estudiante':{
        'nombre':'miguel',
        'notas':
        {'física':7, 
         'historia':8
            }     
        }
    }
}

print(f'El valor de la clave historia es: {diccionario["clase"]["estudiante"]["notas"]["historia"]}')