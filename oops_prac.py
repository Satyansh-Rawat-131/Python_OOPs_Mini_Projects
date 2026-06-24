class Car:

    total_car = 0

    def __init__(self , brand , model):
        self.__brand = brand
        self.model = model
        self.total_car = self.total_car+1

    def fullname(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand + "!"

    def fuel(self):
        return "petrol or diesel"

class E_car(Car):
    def __init__(self , model , brand , battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

    def fuel(self):
        return "electricity"

my_car = Car("toyota", "supra")
my_Ecar = E_car("tesla" , "model S" , "10kg")

# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullname())

print('\n')

# print(my_Ecar.battery_size)
# print(my_Ecar.brand)
# print(my_Ecar.model)
# print(my_Ecar.fullname())
# print(my_car.get_brand())

print(my_car.fuel())
print(my_Ecar.fuel())
print(Car.total_car)