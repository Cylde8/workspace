class Usuario:
    def __init__(self,nombre,apellidos,edad,curso):
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad
        self.curso=curso
    def describir_usuario(self):
        print(f'Nombre: {self.nombre}\nApellidos: {self.apellidos}\nEdad: {self.edad}\nCurso: {self.curso}')
    def saluda_usuario(self):
        print(f'Hola {self.nombre}, me alegra verte.')

ruben=Usuario('Rubén','Tirado Camacho',17,'2ª Bachillerato')
balma=Usuario('Balma','Roda Sastre',20,'3ª Carrera')

ruben.describir_usuario()
ruben.saluda_usuario()
balma.describir_usuario()
balma.saluda_usuario()