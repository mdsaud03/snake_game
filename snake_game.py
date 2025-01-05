from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()  # Snake object initialization
food = Food()  # Food object initialization
scoreboard = Scoreboard()  # Scoreboard object initialization

screen.listen()
screen.onkey(snake.up, "Up")  # Bind the up key to move the snake up
screen.onkey(snake.down, "Down")  # Bind the down key to move the snake down
screen.onkey(snake.left, "Left")  # Bind the left key to move the snake left
screen.onkey(snake.right, "Right")  # Bind the right key to move the snake right

game_is_on = True

while game_is_on:
    screen.update()  # Update the screen to reflect changes
    time.sleep(0.1)  # Control the speed of the snake

    snake.move()  # Move the snake

    # Check if snake has eaten the food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new random location
        snake.extend()  # Add a segment to the snake's body
        scoreboard.increase_score()  # Increase the score

    # Check if snake hits the boundaries of the screen
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False  # End the game if the snake hits the boundary
        scoreboard.game_over()  # Display "Game Over" on the scoreboard

    # Check if the snake collides with itself
    for segment in snake.segments[1:]:  # Skip the first segment (the head)
        if snake.head.distance(segment) < 10:  # Check for collision
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()  # Wait for a click to close the window
