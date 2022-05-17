
"""In order to remove the depency we are gonna need a concept called
an abstract class. Python has a module that supports this abstract
classes (ABC)."""

"""With an abstract class we can define what interface should be that a class
should adhere to so that it's like a contract between different part of the program"""

from abc import ABC, abstractmethod


class Switchable(ABC):
    """This works as the definition of what methods the classes
    that inherits from Switchable should have"""
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")

class ElectricPowerSwitch:

    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = LightBulb()
fan = Fan()
switch = ElectricPowerSwitch(fan)
switch.press()
switch.press()
