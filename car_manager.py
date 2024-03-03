from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shape("square")
            new_car.turtlesize(1, 2, 1)
            new_car.penup()
            new_car.setpos(300, random.randint(-250, 250))
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT





