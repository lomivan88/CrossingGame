import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turn = 0
game_is_on = True
player_t = Player()
screen.listen()
screen.onkeypress(player_t.go, "w")
level_score = Scoreboard()

car = CarManager()
speed = 0.1

while game_is_on:

    if turn == 6:
        car.create_car()
        turn = 0

    car.move_cars()
    time.sleep(speed)
    screen.update()
    turn += 1

    for car_ in car.car_list:
        if player_t.distance(car_.pos()) < 35 and player_t.ycor() + 15 > car_.ycor() > player_t.ycor() - 15:
            game_is_on = False
            level_score.game_over()

    if player_t.is_in_finish():
        for cars in car.car_list:
            cars.clear()

        player_t.go_to_start()
        speed *= 0.5
        level_score.level += 1
        level_score.clear()
        level_score.write_score()


screen.exitonclick()



