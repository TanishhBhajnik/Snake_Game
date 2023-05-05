from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")

    def refresh(self):
        random_x = random.randint(-200,200)
        random_y = random.randint(-200,200)
        self.goto(random_x,random_y)