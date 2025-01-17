from datetime import datetime
import unittest

from CapuletEngine import CapuletEngine
from SternmanEngine import SternmanEngine
from WilloughbyEngine import WilloughbyEngine

from NubbinBattery import NubbinBattery
from SpindlerBattery import SpindlerBattery

from Octoprime import Octoprime
from Carrigan import Carrigan

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30001
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 20000
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 60001
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 40000
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        worn_array = [0.9, 0.8, 0.9, 0.9]
        tire = Octoprime(worn_array)
        self.assertTrue(tire.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        worn_array = [0.1, 0.1, 0.1, 0.1]
        tire = Octoprime(worn_array)
        self.assertFalse(tire.needs_service())

class TestCarrigan(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        worn_array = [0.9, 0.8, 0.9, 0.9]
        tire = Carrigan(worn_array)
        self.assertTrue(tire.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        worn_array = [0.1, 0.1, 0.1, 0.1]
        tire = Carrigan(worn_array)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()

