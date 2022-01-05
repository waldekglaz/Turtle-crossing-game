from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.update()

    def update(self):
        self.write(f"Level {self.level}", align="center", font=("Arial", 18, "bold"))

    def add_point(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 18, "bold"))