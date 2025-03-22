class Car:
    def __init__(self, mileage):
        self.__fuel = 0
        self.mileage = mileage
        self.fuel_consumption_rate = 0.1

    def travel(self, distance):
        if distance < 0 :
            print ("Invalid value for distance")
        else:
            if distance == 0:
                print ("you didn't move")
            elif distance <= self.__fuel / self.fuel_consumption_rate :
                self.mileage += distance
                self.__fuel -= distance * self.fuel_consumption_rate
                print (f"The distance traveled {distance} KM")
                print (f"The remain fuel is {self.__fuel} L")
            elif distance > self.__fuel / self.fuel_consumption_rate:
                self.mileage += self.__fuel / self.fuel_consumption_rate
                print (f"The distance traveled {self.__fuel/self.fuel_consumption_rate}")
                print ("The tank fuel is empty")

    def refuel(self, amount):
        if amount < 0:
            print("Invalid amount")
        else:
            x = 50 - self.__fuel
            if amount > x:
                self.__fuel += x
                print(f"The tank has been filled with {x}L, and now it is 50L")
            elif amount < x:
                self.__fuel += amount
                print(f"The tank has been filled with {amount}L, and now it is {self.__fuel}L")

    def get_remaining_range(self):
        print(f"the maximum distance the car can travel with the current fuel level is {self.__fuel/0.1}L")

    def setter(self, new_amount_of_fuel):
        self.__fuel = new_amount_of_fuel

    def getter(self):
        return self.__fuel

the_car = Car
def refuel():
    amount = input(int("enter the amount of gasoline liters to add, note that the maximum volume of the tank is 50L"))
    the_car.refuel(amount)