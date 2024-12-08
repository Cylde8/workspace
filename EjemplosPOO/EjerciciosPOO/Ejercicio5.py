class Usuario:
    def __init__(self,nombre,apellidos,edad,curso):
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad
        self.curso=curso
        self.intentos_inicio=0
    def incrementar_intentos(self):
        self.intentos_inicio+=1
    def restablecer_intentos(self):
        self.intentos_inicio=0
    def describir_usuario(self):
        print(f'Nombre: {self.nombre}\nApellidos: {self.apellidos}\nEdad: {self.edad}\nCurso: {self.curso}\nIntentos: {self.intentos_inicio}')
    def saluda_usuario(self):
        print(f'Hola {self.nombre}, me alegra verte.')

ruben=Usuario('Rubén','Tirado Camacho',17,'2ª Bachillerato')
balma=Usuario('Balma','Roda Sastre',20,'3ª Carrera')

ruben.describir_usuario()
ruben.incrementar_intentos()
ruben.incrementar_intentos()
ruben.incrementar_intentos()
ruben.describir_usuario()
ruben.restablecer_intentos()
ruben.describir_usuario()