from tire.tire import Tire


class Octoprime(Tire):

    def __init__(self, tire_levels):
        self.tire_levels = tire_levels

    def needs_service(self):
        pressure_sum = 0.0
        for tire_pressure in self.tire_levels:
            pressure_sum += tire_pressure
        if pressure_sum >= 3:
            return True
        return False


