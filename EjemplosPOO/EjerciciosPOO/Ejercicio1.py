class Restaurante:
    def __init__(self, nombre_reastaurante, tipo_cocina):
        self.nombre_restaurante=nombre_reastaurante
        self.tipo_cocina=tipo_cocina
        self.abierto=False
    def abrir_restaurante(self):
        self.abierto=not self.abierto
    def describir_restaurante(self):
        if self.abierto:
            print(f'Restaurante: {self.nombre_restaurante}, Tipo de cocina {self.tipo_cocina} Estado: abierto')
        else:
            print(f'Restaurante: {self.nombre_restaurante}, Tipo de cocina: {self.tipo_cocina} Estado: cerrado')

Restaurante=Restaurante('Bar Alonso', 'bocatas')

Restaurante.abrir_restaurante()
Restaurante.describir_restaurante()
Restaurante.abrir_restaurante()
Restaurante.describir_restaurante()
