vocales=['a', 'e', 'i', 'o', 'u']
def letras(letra):
    if letra in vocales:
        vocal ='True'
    else:
        vocal = 'False'
    return vocal

letra_recivida=input('Dime una letra y te diré si es una vocal o no: ')
print(f'es una vocal?\n{letras(letra_recivida)}')

