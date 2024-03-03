import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # detect collision with cars
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # detect collision with boundary
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

screen.exitonclick()