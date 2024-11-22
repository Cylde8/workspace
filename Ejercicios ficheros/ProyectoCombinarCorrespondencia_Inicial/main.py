#TODO: Crea una carta usando carta_inicial.txt 
#para cada nombre en nombres_invitados.txt
#Cambia el marcador [nombre] con el nombre real.
#Guarda las cartas en la carpeta "ListosParaEnviar".
    
#Pista1: Este método te ayudará: https://www.w3schools.com/python/ref_file_readlines.asp
    #Pista2: Este método también te ayudará: https://www.w3schools.com/python/ref_string_replace.asp
        #Pista3: Este método te ayudará: https://www.w3schools.com/python/ref_string_strip.asp
MARCADOR='[nombre]'

#f_nombres=open('entrada/nombres/nombres_invitados.txt','r')
with open('./entrada/nombres/nombres_invitados.txt') as f_nombres:
    nombres= f_nombres.readlines()
print(nombres)

#f_plantillas= open('entrada/cartas/carta_inicial.txt','r')
with open('./entrada/cartas/carta_inicial.txt') as f_plantillas:
    contenido_carta=f_plantillas.read()

for nombre in nombres:
    nombre=nombre.strip()
    nueva_carta = contenido_carta.replace(MARCADOR, nombre)
    with open(f'./salida/listosParaEnviar/carta_para_{nombre}.txt', mode='w') as carta_finalizada:
        carta_finalizada.write(nueva_carta)

