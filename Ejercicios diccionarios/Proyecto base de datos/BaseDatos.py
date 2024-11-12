# Proyecto sobre estructuras de datos en python: Listas, tuplas, diccionarios y conjuntos 
# Sistema de Bases de Datos para almacenar información de usuarios
# En este proyecto usarás listas y diccionarios
# Partiremos de la definición del diccionario para almacenar la base de datos (usuarios).
# De cada usuario se guardará su apellido y 4 campos: nombre, ocupacion, aficiones y edad.
#Empieza definiendo el diccionario "usuarios"

usuarios={
    'Roda':{
        'Nombre':'Raúl',
        'Ocupación':'Estudiante',
        'Aficiones':['Voleibol', 'Magic', 'Videojuegos'],
        'Edad': 17   
    }
}






# A continuación habrá un bucle en donde se evalúe la entrada del usuario 
# Dentro del bucle se le darán al usuario 4 opciones: listar usuarios, añadir un usuario, borrar un usuario, buscar un usuario
# Dependiendo de lo que conteste el usuario se hará lo que dice esa opción.

while True:
    elige_opcion = input("1 - listar usuarios, 2 - añadir un usuario, 3 - borrar un usuario, 4 - buscar un usuario, 5 - salir: ")
    match elige_opcion:
        case '1':
            print('** Todos los usuarios **')
            for apellido in usuarios:
                print(f'Apellido: {apellido}')
                informacion_usuario = usuarios[apellido]
                for clave, valor in informacion_usuario.items():
                    print(f'{clave.capitalize()}:{valor}')
        case '2':
            apellido=input('Introduce el apellido: ')
            if 'apellido' in usuarios:
                print('El usuario ya existe.\n')
            else:
                nombre=input('Introduce el nombre: ')
                ocupacion=input('Introduce la ocupación: ')
                aficiones=input('Introduce las aficiones: '.split(','))
                edad=input('Introducre la edad: ')
                usuarios[apellido]={
                    'Nombre':nombre,
                    'Ocupación':ocupacion,
                    'aficiones':aficiones,
                    'edad':edad
                }
                print('El usuario ha sido añadido.')
#        case '3':

#        case '4':

        case '5':
            break            


