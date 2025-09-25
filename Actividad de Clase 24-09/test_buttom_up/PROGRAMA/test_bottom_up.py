import pytest

from PROGRAMA.modulos.calculadora_impuestos import CalculadoraImpuestos
from PROGRAMA.modulos.calculadora_bonos import CalculadoraBonos
from PROGRAMA.modulos.calculadora_deducciones import CalculadoraDeducciones
from PROGRAMA.drivers.test_driver import DriverNomina


class TestNivelBase:
    """Nivel 1: Prueba módulos atómicos"""

    def setup_method(self):
        self.calc = CalculadoraImpuestos()

    def test_isr_salario_bajo(self):
        salario = 8000
        resultado = self.calc.calcular_isr(salario)
        assert resultado == 400  # 5% de 8000

    def test_isr_salario_medio(self):
        resultado = self.calc.calcular_isr(15000)
        assert resultado == 1500  # 10% de 15000

    def test_seguro_social(self):
        resultado = self.calc.calcular_seguro_social(10000)
        assert resultado == 625  # 6.25% de 10000


class TestIntegracion:
    """Nivel 2: Pruebas de integración usando DriverNomina"""

    def setup_method(self):
        self.impuestos = CalculadoraImpuestos()
        self.bonos = CalculadoraBonos()
        self.deducciones = CalculadoraDeducciones()
        self.driver = DriverNomina(self.impuestos, self.bonos, self.deducciones)

    def test_nomina_basica(self):
        salario = 10000
        rendimiento = 0.5
        faltas = 2

        resultado = self.driver.ejecutar(salario, rendimiento, faltas)

        #Calculos Esperados
        assert resultado["ISR"] == 1000
        assert resultado["SeguroSocial"] == 625
        assert resultado["Bonos"] == 500       # 10000 * 0.5 * 0.1
        assert resultado["Deducciones"] == (10000/30) * 2

    def test_nomina_sin_faltas_y_sin_bonos(self):
        salario = 8000
        rendimiento = 0.0
        faltas = 0

        resultado = self.driver.ejecutar(salario, rendimiento, faltas)

        #Calculos Esperados
        assert resultado["ISR"] == 400
        assert resultado["SeguroSocial"] == 500
        assert resultado["Bonos"] == 0
        assert resultado["Deducciones"] == 0
