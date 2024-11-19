alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def cesar(texto,desplazamiento,direccion):
    texto_cifrado=''
    
'''
def codifica(texto_plano, desplazamiento):
    texto_cifrado=''
    for letra in texto_plano:
        posicion = alfabeto.index(letra)
        nueva_posicion = (posicion+desplazam) % 27
        texto_cifrado += alfabeto[nueva_posicion]
    print(f'El texto codificado es: {texto_cifrado}')
def decodifica(texto_codificado, desplazamiento):
    texto_plano=''
    for letra in texto_codificado:
        posicion = alfabeto.index(letra)
        nueva_posicion = (posicion-desplazam) % 27
        texto_plano += alfabeto[nueva_posicion]
    print(f'El texto codificado es: {texto_plano}')
'''
direccion = input("Escribe 'codifica' para codificar o 'decodifica' para decodificar: ")
texto = input("Escribe tu mensaje: ").lower()
desplazam = int(input("Escribe un número para el desplazamiento: "))

#TODO-1: Crea una funcion llamada 'codifica' que coja el 'texto' y 'desplazamiento' como entradas.

    #TODO-2: Dentro de la función 'codifica', desplaza cada letra del 'texto' hacia adelante en el alfabeto
    # la cantidad desplazam e imprime el texto codificado.  
    #ejemplo: 
    #texto_plano = "hola"
    #desplazamiento = 5
    #texto_cifrado = "mtpf"
    #print output: "El texto codificado es mtpf"
# Ayuda: indice de una lista en Python: https://www.w3schools.com/python/ref_list_index.asp  

#TODO-3: Llama a la función codifica y pasa lo que ha introducido el usuario. 
# Deberías ser capaz de probar el código y codificar un mensaje. 
if direccion == 'codifica':
    codifica(texto,desplazam)
else:
    decodifica(texto,desplazam)

