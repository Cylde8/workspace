with open('ficheros/temperaturas.dat') as f:
    for linea in f:
        min_temps, max_temps = linea.strip().split()
        print(min_temps, max_temps)
