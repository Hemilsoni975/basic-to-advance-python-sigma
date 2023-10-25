





print("HYBRID-INHERITANCE :- MORE THAN ONE TYPE OF INHERITANCE")

class vehicle:
    def veh(self):
        print("I am vehicle class")

class bike(vehicle):
    def two(self):
        print("I am bike class inheriting vehicle class")

class car(vehicle):
    def four(self):
        print("I am car class inheritng vehicle class")

class yamaha(bike):
    def yam(self):
        print("I am yamaha and can inherit bike class and main vehicle class")

class suzuki(car):
    def suz(self):
        print("I am suzuki and can inherit car class and main vehicle")

class owner(yamaha,suzuki):
    def own(self):
        print("I am the owner of yamaha and suzuki and can inherit all the class properties")


y = yamaha()
y.veh()
y.two()
y.yam()

s = suzuki()
s.veh()
s.four()
s.suz()

o = owner()
o.veh()
o.two()
o.yam()
o.four()
o.suz()
o.own()