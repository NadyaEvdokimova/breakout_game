from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.position = (20, -260)
        self.goto(self.position)
        self.speed = 0
        self.move_left = False
        self.move_right = False

    def right_move(self):
        if self.xcor() < 185:
            self.move_right = True
            x_current = self.xcor()
            self.setx(x_current + 15)

    def right_move_end(self):
        if self.xcor() < 185:
            self.move_right = False

    def left_move(self):
        if self.xcor() > - 190:
            self.move_left = True
            x_current = self.xcor()
            self.setx(x_current - 15)

    def left_move_end(self):
        if self.xcor() > - 190:
            self.move_left = True

    def refresh(self):
        self.goto(self.position)
