from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(200, 220)
        self.write(f'Score: {self.score}', align="right",
                   font=("Courier", 20, "normal"))

    def point(self, color):
        if color == 'yellow':
            self.score += 1
        elif color == 'green':
            self.score += 3
        elif color == 'orange':
            self.score += 5
        elif color == 'red':
            self.score += 7
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -130)
        self.write(f"GAME OVER\nYour Score is {self.score}", align="center",
                   font=("Courier", 20, "normal"))
