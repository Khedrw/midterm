class Car:
    def __init__(self, mileage):
        self.__fuel = 0
        self.mileage = 0
        self.fuel_consumption_rate = 0.1

    def travel(self, distance):
        if self.__fuel == 0:
            print ("Fill your tank first!")
        else:
            if distance < 0:
                print("Invalid value for distance")
            elif distance == 0:
                print ("you kidding me!")
            elif distance <= self.__fuel / self.fuel_consumption_rate :
                self.mileage += distance
                self.__fuel -= distance * self.fuel_consumption_rate
                print (f"The distance traveled {distance} KM")
                print (f"The remain fuel is {self.__fuel} L")
            elif distance > self.__fuel / self.fuel_consumption_rate:
                self.mileage += self.__fuel / self.fuel_consumption_rate
                print (f"The distance traveled {self.__fuel/self.fuel_consumption_rate}KM of {distance}KM")
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

the_car = Car(0)

def refuel():
    amount = int(input("enter the amount of gasoline liters to add, note that the maximum volume of the tank is 50L "))
    the_car.refuel(amount)

def travel():
    distance = int(input("Enter the distance you want to travel, please. "))
    the_car.travel(distance)

def gettheremainingrange():
    the_car.get_remaining_range()

def setter():
    a = 51
    while a < 0 or a > 50:
        print ("Invalid values, note that the tank range is between (0 ; 50)L")
        a = int(input("Enter the new value for the tank "))
    the_car.setter(a)

def getter():
    the_car.getter()

action = None

def prompt():
    print("======================")
    print("Enter 0 to refuel the car.")
    print("Enter 1 to input the distance.")
    print("Enter 2 to get the remaining range.")
    print("Enter 3 to get the current fuel level.")
    print("Enter 4 to set the fuel level.")
    print("Enter 5 to exit")
    action = int(input("Choice: "))
    print("======================")
    return action

while action != 5:
    action = prompt()
    if action == 0:
        refuel()
    elif action ==1:
        travel()
    elif action == 2:
        gettheremainingrange()
    elif action == 3:
        getter()
    elif action == 4:
        setter()
    elif action == 5:
        print("Program Exit")