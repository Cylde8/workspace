#programa que tras crear una lista te crea su invertida
lista=[]
n_palabras=int(input('Dígame cuantas palabras tiene la lista: '))
for i in range(0,n_palabras):
    palabra=input(f'Dígame la palabra {i+1}: ')
    lista.append(palabra)
lista_invertida=list(reversed(lista))
print(f'La lista creada es: {lista}')
print(f'La lista invertida es: {lista_invertida}')