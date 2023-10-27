from abc import ABC,abstractmethod

class Vehicle(ABC):

    def __init__(self, n):
        self.no_of_tyres = n

    @abstractmethod
    def display(self):
        pass