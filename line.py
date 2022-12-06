from turtle import Turtle

class Line (Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pensize(10)
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        for i in range(17):
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(20)
