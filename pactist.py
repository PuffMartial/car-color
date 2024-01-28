class Car:
    color = None
def change_colors(car, color):
    car.color = color

car_1 = Car()
car_2 = Car()
Car_3 = Car()

change_colors(car_1,"Red")
change_colors(car_2,"White")
change_colors(car_3,"Blue")

print(car_1.color)
print(car_2.color)
print(car_3.color)