class CalculadoraBonos:
    def calcular(self, salario_base, rendimiento):
        """
        Calcula un bono según el rendimiento.
        - rendimiento: valor entre 0 y 1 (0% - 100%)
        """
        return salario_base * rendimiento * 0.1