#programa que crea una lista de números pares
lista=[]
numero=int(input('Dígame un número: '))
for i in range(1,numero):
    if i%2==0:
        lista.append(i)
print(f'Pares hasta {numero}: {lista}')