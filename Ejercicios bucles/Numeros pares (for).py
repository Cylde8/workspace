#Programa que pide dos numerps y te escribe los numeros pares entre estos dos
inicio=int(input('Dame el valor inicial: '))
fin=int(input('Dame el valor final: '))
numeros_pares=[]
for i in range(inicio,fin+1):
    if i%2==0:
        numeros_pares.append(i)
print(numeros_pares)