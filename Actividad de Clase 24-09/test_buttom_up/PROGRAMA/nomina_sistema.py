from modulos import CalculadoraBonos, CalculadoraDeducciones, CalculadoraImpuestos

class NominaSistema:
    """Sistema integrado usando modulos ya probados"""

    def __init__(self):
        # Integrar modulos base
        self.calc_impuestos = CalculadoraImpuestos()
        self.calc_bonos = CalculadoraBonos()
        self.calc_deducciones = CalculadoraDeducciones()

    def calcular_nomina_neta(self, empleado):
        salario = empleado['salario_base']

        # Usar modulos ya validados
        isr = self.calc_impuestos.calcular_isr(salario)
        seguro = self.calc_impuestos.calcular_seguro_social(salario)
        bonos = self.calc_bonos.calcular_bonos(empleado)

        return salario + bonos - isr - seguro