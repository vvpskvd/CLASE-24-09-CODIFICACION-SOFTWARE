class DatabaseStub:
    """Stub que simula base de datos"""

    def __init__(self):
        # Simulamos qué libros están disponibles o no
        self.libros_disponibles = {1: True, 2: True, 3: False}
        self.prestamos_registrados = []

    def libro_disponible(self, libro_id):
        return self.libros_disponibles.get(libro_id, False)

    def registrar_prestamo(self, usuario_id, libro_id):
        self.prestamos_registrados.append((usuario_id, libro_id))