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
    elige_opcion = input("1 - listar usuarios, 2 - añadir un usuario, 3 - borrar un usuario, 4 - buscar un usuario, 5 - guardar, 6 - salir: ")
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
            if apellido in usuarios:
                print('El usuario ya existe.\n')
            else:
                nombre=input('Introduce el nombre: ')
                ocupacion=input('Introduce la ocupación: ')
                aficiones=input('Introduce las aficiones separadas por comas: ').split(',')
                edad=input('Introducre la edad: ')
                usuarios[apellido]={
                    'Nombre':nombre,
                    'Ocupación':ocupacion,
                    'aficiones':aficiones,
                    'edad':edad
                }
                print('El usuario ha sido añadido.\n')
        case '3':
            borrar=input('Introduce el apellido: ')
            if borrar not in usuarios:
                print('El usuario no existe.\n')
            else:
                del usuarios[borrar]
                print(f'Se ha borrado el usuario {borrar}\n')

        case '4':
            buscar=input('Introduce el usuario a buscar: ')
            if buscar not in usuarios:
                print('El usuario no existe.\n')
            else:
                print('El usuario existe.\n')
#        case '5':

#        case '6':
#            break            


