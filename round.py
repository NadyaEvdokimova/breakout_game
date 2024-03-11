from turtle import Turtle


class Round(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.round = 1
        self.update_round()

    def update_round(self):
        self.clear()
        self.goto(200, 250)
        self.write(f'Round: {self.round}/2', align="right",
                   font=("Courier", 20, "normal"))

    def next_round(self):
        self.round += 1
        self.update_round()
