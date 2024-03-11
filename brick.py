from turtle import Turtle


class Brick:
    def __init__(self):
        self.bricks = []
        self.rows()

    def rows(self):
        for all_pos in range(0, 240, 60):
            for y_pos in range(all_pos, all_pos+60, 30):
                for position in range(-235, 230, 65):
                    brick = Turtle('square')
                    brick.penup()
                    brick.shapesize(stretch_wid=1, stretch_len=3)
                    if y_pos <= 30:
                        brick.color('yellow')
                    elif y_pos <= 90:
                        brick.color('green')
                    elif y_pos <= 150:
                        brick.color("orange")
                    elif y_pos <= 210:
                        brick.color("red")
                    brick.goto(x=position, y=y_pos)
                    self.bricks.append(brick)

    def exclude_brick(self, del_brick):
        self.bricks[del_brick].ht()
        del self.bricks[del_brick]


        

