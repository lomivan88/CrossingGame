from turtle import Turtle
from random import choice,randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.turtlesize(stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.setx(x=300)
        new_car.sety(randint(-250, 250))
        self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.setx(car.xcor() - STARTING_MOVE_DISTANCE)
            if car.xcor() < -350:
                self.car_list.pop(self.car_list.index(car))


