class Restaurante:
    def __init__(self, nombre_reastaurante, tipo_cocina):
        self.nombre_restaurante=nombre_reastaurante
        self.tipo_cocina=tipo_cocina
        self.abierto=False
        self.servido=0
    def abrir_restaurante(self):
        self.abierto=not self.abierto
    def describir_restaurante(self):
        if self.abierto:
            print(f'Restaurante: {self.nombre_restaurante}, Tipo de cocina {self.tipo_cocina} Estado: abierto')
            print(f'Se ha servido a {self.servido} personas')
        else:
            print(f'Restaurante: {self.nombre_restaurante}, Tipo de cocina: {self.tipo_cocina} Estado: cerrado')
    def establecer_como_servido(self,servicios):
        if servicios>=self.servido:
            self.servido=servicios
        else:
            print('No se puede disminuir el número de gente a la que has servido')
    def incrementar_num_servido(self,servido_ahora):
        self.servido+=servido_ahora

Restaurante=Restaurante('Bar Alonso', 'bocatas')

Restaurante.abrir_restaurante()
Restaurante.describir_restaurante()
Restaurante.establecer_como_servido(10)
Restaurante.describir_restaurante()
Restaurante.incrementar_num_servido(5)
Restaurante.describir_restaurante()
Restaurante.abrir_restaurante()
Restaurante.describir_restaurante()
