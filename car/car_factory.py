from typing import List
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from datetime import date, datetime
from car.car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
# from tires.tires import Tires
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires
from tires.tires import Tires


class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear:int) -> Car:
        return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date), CarriganTires(tire_wear))

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear:int) -> Car:
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date), CarriganTires(tire_wear))

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_is_on:bool, tire_wear:int) -> Car:
        return Car(SternmanEngine(warning_light_is_on), SpindlerBattery(current_date, last_service_date), OctoprimeTires(tire_wear))

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear:int) -> Car:
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date), OctoprimeTires(tire_wear))

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear:int) -> Car:
        return Car(	CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date), OctoprimeTires(tire_wear))