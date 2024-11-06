#programa que te ordena una lista por orden alfabético
lista=[]
n_palabras=int(input('Dígame cuántas palabras tiene la lista: '))
for i in range(0,n_palabras):
    palabra=input(f'Digame la palabra {i+1}: ')
    lista.append(palabra)
print(f'La lista creada es: {lista}')
lista=sorted(lista)
print(f'La lista ordenada es: {lista}')