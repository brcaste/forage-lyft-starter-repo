from battery.battery import Battery
from engine.engine import Engine
from serviceable import Serviceable


class Car(Serviceable, Battery, Engine):
    engine_cls = Engine
    battery_cls = Battery

    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        pass
