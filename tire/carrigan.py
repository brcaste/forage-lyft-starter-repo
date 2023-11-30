from tire.tire import Tire
from array import *


class Carrigan(Tire):

    def __init__(self, tire_levels):
        self.tire_levels = tire_levels

    def needs_service(self):
        for pressure in self.tire_levels:
            if pressure >= 0.9:
                return True
        return False
