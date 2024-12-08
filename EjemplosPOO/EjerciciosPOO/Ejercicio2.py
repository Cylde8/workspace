class Restaurante:
    def __init__(self, nombre_reastaurante, tipo_cocina):
        self.nombre_restaurante=nombre_reastaurante
        self.tipo_cocina=tipo_cocina
        self.abierto=False
    def abrir_restaurante(self):
        self.abierto=not self.abierto
    def describir_restaurante(self):
        if self.abierto:
            print(f'Restaurante: {self.nombre_restaurante}, Tipo de cocina:f {self.tipo_cocina} Estado: abierto')
        else:
            print(f'Restaurante: {self.nombre_restaurante}, Tipo de cocina: {self.tipo_cocina} Estado: cerrado')

Restaurante1=Restaurante('Bar Alonso', 'bocatas')
Restaurante2=Restaurante('El Galeon','mediterranea')
Restaurante3=Restaurante('Pizzeria Italia','Italiana')

Restaurante1.abrir_restaurante()
Restaurante1.describir_restaurante()
Restaurante1.abrir_restaurante()
Restaurante1.describir_restaurante()

Restaurante2.abrir_restaurante()
Restaurante2.describir_restaurante()
Restaurante2.abrir_restaurante()
Restaurante2.describir_restaurante()

Restaurante3.abrir_restaurante()
Restaurante3.describir_restaurante()
Restaurante3.abrir_restaurante()
Restaurante3.describir_restaurante()