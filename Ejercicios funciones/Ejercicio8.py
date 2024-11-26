meses31=[1,3,5,7,8,10,12]
meses30=[4,6,9,11]
def DiasDelMes(mes,bisiesto):
    if mes in meses31:
        dias=31
    elif mes in meses30:
        dias=30
    else:
        if bisiesto=='bisiesto':
            dias=29
        else:
            dias=28
    return dias

def EsBisiesto(año):
    if año%4==0 and (año%100!=0 or año%400==0):
        año='bisiesto'
    else:
        año='no bisiesto'
dia=int(input('Di un día: '))
mes=int(input('Di un mes: '))
año=int(input('Di un año: '))
anyo=int(input('Di un año y te diré el día juliano de la fecha previamente indicada: '))
Total_dias=dia
while(anyo<año):
    anyo+=1
    for i in range(1.13):
        dias_del_mes=DiasDelMes(i,EsBisiesto(anyo))
        Total_dias+=dias_del_mes
for i in range(1,mes):
    Total_dias+=DiasDelMes(i,EsBisiesto(anyo))


print(f'El día juliano es {Total_dias}')