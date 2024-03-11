from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from life import Life
from scoreboard import Scoreboard
from round import Round
import time

screen = Screen()
screen.bgcolor('black')
screen.title('Breakout Game')
screen.setup(width=500, height=600)
screen.tracer(0)
paddle = Paddle()
ball = Ball()
brick = Brick()
life = Life()
scoreboard = Scoreboard()
game_round = Round()
bricks_collisions = 0
colors = []

# Make paddle movement
screen.listen()
screen.onkeypress(paddle.right_move, "Right")
screen.onkeyrelease(paddle.right_move_end, "Right")
screen.onkeypress(paddle.left_move, "Left")
screen.onkeyrelease(paddle.left_move_end, "Left")

# Game starts
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with left and right walls
    if ball.xcor() > 230 or ball.xcor() < -230:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 70 and ball.ycor() < -230:
        ball.bounce_y()

    # Detect collision with bricks
    for each_brick in brick.bricks:
        if ball.distance(each_brick) < 30:
            bricks_collisions += 1
            ball.bounce_y()
            brick_index = brick.bricks.index(each_brick)
            brick.exclude_brick(brick_index)
            colors.append(each_brick.fillcolor())
            colors_check = {color: colors.count(color) for color in colors}
            # Add point for score
            scoreboard.point(each_brick.fillcolor())
            # Speed of ball rises after: 4 collisions with bricks, 12 collisions with bricks, collision with
            # first orange brick and with red brick - after first red hit - paddle resized
            if each_brick.fillcolor() == 'orange' and colors_check['orange'] == 1:
                ball.move_speed *= 0.9
            if each_brick.fillcolor() == 'red' and colors_check['red'] == 1:
                paddle.shapesize(stretch_wid=1, stretch_len=2)
                ball.move_speed *= 0.9
            if bricks_collisions == 4:
                ball.move_speed *= 0.9
            elif bricks_collisions == 12:
                ball.move_speed *= 0.9
    # Remove life if ball is missed: ball and paddle start from starting positions
    if ball.ycor() < -250:
        life.remove_life()
        ball.refresh()
        paddle.refresh()
        bricks_collisions = 0
        ball.move_speed = 0.1
        colors = []
        if len(life.lives) == 0:
            screen.update()
            scoreboard.game_over()
            game_is_on = False

    # if no more bricks - go to the second round
    if not brick.bricks:
        game_round.next_round()
        ball.refresh()
        paddle.refresh()
        bricks_collisions = 0
        ball.move_speed = 0.1
        paddle.shapesize(stretch_wid=1, stretch_len=4)
        colors = []
        brick.rows()

    # if two screens are cleared - game over
    if game_round.round > 2:
        screen.update()
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
