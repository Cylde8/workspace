def histograma(lista):
    for i in lista:
        print('*'*int(i))
numeros=input('Introduce varios números separados por comas: ').split(',')
histograma(numeros)
