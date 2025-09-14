import random
from turtle import Turtle

"""creating a food class """
class Food(Turtle):

    def __init__(self):
        # defining the shape,and features of the food,turtle
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    """method to make it possible for the food turt to appear randomly in the screen"""
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)