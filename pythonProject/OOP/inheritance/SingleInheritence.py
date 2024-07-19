class Vehicle1:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_vehicle(self):
        print("from vehicle - ", self.mileage)
        print("from vehicle - ", self.cost)
        print("vehicle")


class Car(Vehicle1):

    def __init__(self, mileage, cost, tyres, hp1):
        super().__init__(mileage, cost)
        self.tyres = tyres
        self.hp1 = hp1

    def show_car_details(self):
        print("car", self.hp1)
        print("car")


v = Vehicle1(100, 50)
v.show_vehicle()

c = Car(100, 200, 20, 2)
c.show_car_details()
c.show_vehicle()
