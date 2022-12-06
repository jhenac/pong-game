from turtle import Turtle
ALIGNMENT = "center"
COLOR = "white"
font_tuple = ("Arial", 70, "normal")

class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.goto(0, 180)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=font_tuple)
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=font_tuple)

    def increase_right_score(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_left_score(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

