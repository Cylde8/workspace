#obtener el valor minimo de un diccionario
diccionario={
    'Matematicas':7,
    'Física':8,
    'Historia':9
}
minimo=10
for asignatura,nota in diccionario.items():

    if nota<minimo:
        minimo=nota
        asignatura_min=asignatura
print(f'El minimo es:  {asignatura_min}')