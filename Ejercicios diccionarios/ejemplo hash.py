import hashlib
salida = hashlib.sha256(b'El Libro De Python').hexdigest()
print(salida)