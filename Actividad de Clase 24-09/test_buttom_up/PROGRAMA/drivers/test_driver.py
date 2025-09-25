class DriverNomina:
    """Driver para ejecutar pruebas en módulos base"""
    
    def __init__(self, impuestos, bonos, deducciones):
        self.impuestos = impuestos
        self.bonos = bonos
        self.deducciones = deducciones

    def ejecutar(self, salario, rendimiento, faltas):
        return {
            "ISR": self.impuestos.calcular_isr(salario),
            "SeguroSocial": self.impuestos.calcular_seguro_social(salario),
            "Bonos": self.bonos.calcular(salario, rendimiento),
            "Deducciones": self.deducciones.calcular(salario, faltas),
        }