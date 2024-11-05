#programa que tras crear una lista te crea su invertida
lista=[]
lista_2=[]
n_palabras=int(input('Dígame cuantas palabras tiene la lista: '))
for i in range(0,n_palabras):
    palabra=input(f'Dígame la palabra {i+1}: ')
    lista.append(palabra)
for i in range(n_palabras-1,-1,-1):
    lista_2.append(lista[i])
print(f'La lista creada es: {lista}')
print(f'La lista invertida es: {lista_2}')