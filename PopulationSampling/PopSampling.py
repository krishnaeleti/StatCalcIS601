from Calculator.Calculator import Calculator
from PopulationSampling.CochransFormula import cochran

class PopSampling(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def cochran(self, z, p, q, e):
        self.result = cochran(z, p, q, e)
        return self.result