# Turtle crossing
# 1. Create screen V
# 2. create turtle V
# 3. Determine its movement V
# 4. Create class of rectangles V
# 5. Determine movement of rectangles V
# 6. Determine  when collision occursV
# 7. Get hold of the score

import turtle as t
import time
from player import Player
from car import Car
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = Car()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_level()

    car.create_car()
    car.move()

    # Detect collision with car
    for car_object in car.all_cars:
        if car_object.distance(player) < 15:
            game_is_on = False
            scoreboard.game_is_over()

    # detect if turtle has crossed
    if player.has_crossed():
        player.go_back()
        car.speed_up()
        scoreboard.increase_level()

screen.exitonclick()
