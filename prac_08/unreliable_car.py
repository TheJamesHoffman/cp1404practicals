from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, fuel, name, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        reliable_check = randint(1, 100)
        if reliable_check >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
