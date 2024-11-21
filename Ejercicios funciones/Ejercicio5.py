def tiempo_horas_min_seg(s):
    h=s//3600
    min=(s%3600)//60
    s=(s%3600)%60 
    print(f'El total es: {h} horas {min} minutos {s} segundos')

def tiempo_segundos(h,min,s):
    h*=3600
    min*=60
    total=h+min+s
    print(f'El total es de {total} segundos')


eleccion=input('Pulse "1" si desea cambiar de segundos a horas, minutos y segundos; pulse "2" si desa cambiar de horas, minutos y segundos a segundos: ')
if eleccion== '1':
    segundos=int(input('Dame una cantidad de segundos: '))
    tiempo_horas_min_seg(segundos)
else:
    horas=int(input('Dime las horas: '))
    minutos=int(input('Dime los minutos: '))
    segundos=int(input('Dime los segundos: '))
    tiempo_segundos(horas,minutos,segundos)