import string
import random

"""
    NOTE: Information Expert: where is information store and how we access this.
    When we have defined the logical structure of your information, we can start
    to group our code around that. That will leads a lower coupling because the
    code is closer to the information that it uses.
"""

class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool

    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")

class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print("Registration complete. Vehicle information:")
        print(f"ID: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:

    vehicule_info = { }

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicule_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def __init__(self):
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BWM 5", False, 45000)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand: string):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicule_info[brand])


class Application:

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        # create a vehicle
        return registry.create_vehicle(brand)


app = Application()
vehicle = app.register_vehicle("Volkswagen ID3")
vehicle.print()