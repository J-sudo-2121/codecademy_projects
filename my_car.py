# Importing Multiple Classes from a Module
from car import Car 
# Using Aliases
from electric_car_ex_2 import ElectricCar as EC

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()