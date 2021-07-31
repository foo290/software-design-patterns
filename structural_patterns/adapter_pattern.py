class Car:
    def __init__(self):
        self.name = "Tesla"
        self.wheels = 4

    def four_wheeler(self):
        print(f"This is {self.name}, has {self.wheels} wheels")


class Bike:
    def __init__(self):
        self.name = "Duke"
        self.wheels = 2

    def two_wheeler(self):
        print(f"This is {self.name}, has {self.wheels} wheels")


class Truck:
    def __init__(self):
        self.name = "Tesla Truck"
        self.wheels = 18

    def many_wheels(self):
        print(f"This is {self.name}, has {self.wheels} wheels")


class VehicleAdapter:
    _initialized = False

    def __init__(self, vehicle, **kwargs):
        self.vehicle = vehicle
        self.__dict__.update(kwargs)
        self._initialized = True

    def __getattr__(self, item):
        return getattr(self.vehicle, item)

    def __setattr__(self, key, value):
        if not self._initialized:
            super().__setattr__(key, value)
        else:
            setattr(self.vehicle, key, value)


if __name__ == '__main__':
    vehicle_adapters = []

    car = Car()
    vehicle_adapters.append(VehicleAdapter(car, wheels=car.four_wheeler))

    bike = Bike()
    vehicle_adapters.append(VehicleAdapter(bike, wheels=bike.two_wheeler))

    truck = Truck()
    vehicle_adapters.append(VehicleAdapter(truck, wheels=truck.many_wheels))

    for eachAdapter in vehicle_adapters:
        # Now call only single method to call each different methods
        eachAdapter.wheels()

