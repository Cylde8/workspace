#Programa que te permite crear una lista y eliminar elementos
lista=[]
n_palabras=int(input('Dígame cuántas palabras tiene la lista: '))
for i in range(0,n_palabras):
    palabra=input(f'Digame la palabra {i+1}: ')
    lista.append(palabra)
print(f'La lista creada es: {lista}')
eliminar=input('Palabra a eliminar: ')
while eliminar in lista:
    lista.remove(eliminar)
print(f'La lista ahora es: {lista}')