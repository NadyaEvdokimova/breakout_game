from turtle import Turtle


class Life:
    def __init__(self):
        self.lives = []
        self.get_lives()

    def get_lives(self):
        for x_pos in range(-230, -150, 30):
            life = Turtle()
            life.shape('circle')
            life.color('firebrick2')
            life.penup()
            life.goto((x_pos, 280))
            self.lives.append(life)

    def remove_life(self):
        lives_number = len(self.lives)
        self.lives[lives_number - 1].ht()
        del self.lives[lives_number - 1]
