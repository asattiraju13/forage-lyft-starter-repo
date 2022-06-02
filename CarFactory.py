from CapuletEngine import CapuletEngine
from NubbinBattery import NubbinBattery
from SpindlerBattery import SpindlerBattery
from SternmanEngine import SternmanEngine
from WilloughbyEngine import WilloughbyEngine
from Octoprime import Octoprime
from Carrigan import Carrigan
from car import Car


class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, worn_array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = Octoprime(worn_array)
        return Car(engine, battery, tire)

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, worn_array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = Octoprime(worn_array)
        return Car(engine, battery, tire)

    def create_palindrome(current_date, last_service_date, warning_light_on, worn_array):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = Carrigan(worn_array)
        return Car(engine, battery, tire)

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, worn_array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = Carrigan(worn_array)
        return Car(engine, battery, tire)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, worn_array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = Carrigan(worn_array)
        return Car(engine, battery, tire)
