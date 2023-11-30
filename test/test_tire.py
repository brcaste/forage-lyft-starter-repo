import unittest
from tire.carrigan import Carrigan
from tire.octoprime import Octoprime


class TestOctoprime(unittest.TestCase):
    def test_tire_needs_service(self):
        pressure_levels = [1.0, 1.0, 1.0, 0.5]
        tire = Octoprime(pressure_levels)
        self.assertTrue(tire.needs_service())
    def test_tire_does_not_need_service(self):
        pressure_levels = [0.2, 0.5, 1.0, 0.5]
        tire = Octoprime(pressure_levels)
        self.assertFalse(tire.needs_service())

class TestCarrigan(unittest.TestCase):
    def test_tire_needs_service(self):
        pressure_levels = [0.5, 0.8, 0.9, 0.5]
        tire = Carrigan(pressure_levels)
        self.assertTrue(tire.needs_service())
    def test_tire_does_not_need_service(self):
        pressure_levels = [0.7, 0.6, 0.8, 0.5]
        tire = Octoprime(pressure_levels)
        self.assertFalse(tire.needs_service())
