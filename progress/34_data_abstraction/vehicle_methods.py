from vehicle_library import Vehicle

class Bike(Vehicle):

    def __init__(self ,n, color):
        super().__init__(n)
        self.color = color
    def display(self):
        print(f"start with kick.\nI have {self.no_of_tyres} tyres.\nI have {self.color} color.")

class Car(Vehicle):

    def __init__(self , n, g):
        super().__init__(n)
        self.no_of_gear = g

    def display(self):
        print(f"start with key.\nI have {self.no_of_tyres} tyres.\nI have {self.no_of_gear} gear")

class Auto(Vehicle):

    def __init__(self,n):
        super().__init__(n)

    def display(self):
        print(f"start with pulling rod.\nI have {self.no_of_tyres} tyres")

