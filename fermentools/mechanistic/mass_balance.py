from . import YeastModel

class MassBalance:
    def __init__(self, microbial_kinetics: YeastModel, inlet: float, outlet: float):
        self.microbial_kinetics = microbial_kinetics
        self.inlet = inlet
        self.outlet = outlet



    def calculate(self, concentrations: list, time: float) -> list:
        """
        Calculates the mass balance for a given kinetic rate list.
        """
        return self.microbial_kinetics.calculate_rates(concentrations[0], concentrations[1])
