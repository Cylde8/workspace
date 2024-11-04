#programa que pide una cantidad a introducir. Se preguntan esos numeros y dice el mayor, el menor y la media
cantidad=int(input('¿Cuántos números vas a introducir?: '))
lista=[]
for i in range(0,cantidad):
    numero=int(input('Dime el número: '))
    lista.append(numero)
    maximo=max(lista)
    minimo=min(lista)
    media=float(sum(lista)/len(lista))
print(f'El número mínimo es: {minimo}')
print(f'El número máximo es: {maximo}')
print(f'La media de los números introducidos es: {media}')
