#Programa que calcula tu IMC
peso=float(input('Introduzca su peso en kg: '))
altura=float(input('Introduzca su altura en metros: '))
imc=round(peso/(altura*altura),2)
print(f'Su indice de masa corporal es: {imc}')
if imc<18.5:
    print('Tiene insuficiencia ponderal')
elif 1.85<=imc<25:
    print('Está en el intervalo normal')
elif 25<=imc<30:
    print('Tiene sobrepeso')
else:
    print('Tiene obesidad')
