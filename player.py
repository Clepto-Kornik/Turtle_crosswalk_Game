from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.go_back()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_back(self):
        self.goto(STARTING_POSITION)

    def has_crossed(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False
