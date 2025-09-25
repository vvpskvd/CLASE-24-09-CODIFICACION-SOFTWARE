class CalculadoraDeducciones:
    def calcular(self, salario_base, faltas):
        """
        Calcula deducciones según las faltas.
        - faltas: número de días no trabajados
        """
        return faltas * (salario_base / 30)