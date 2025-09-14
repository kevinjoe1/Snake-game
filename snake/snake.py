from turtle import Turtle
SQUARES_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
"""creating a snake class """
class Snake:

    def __init__(self):
        # Creating an empty list to store the turtles
        self.segments = []
        self.create_snake()
        # creating the first turtle as head of the turtle
        self.head = self.segments[0]

    def create_snake(self):
        for position in SQUARES_POSITION:
           self.add_snake(position)

# Adding multiple turtles to make a snake like figure

    def add_snake(self,position):
        new_squares = Turtle(shape='square')
        new_squares.penup()
        new_squares.color('white')
        new_squares.goto(position)
        self.segments.append(new_squares)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self,):
        # method to extend the snake when collision with food
        self.add_snake(self.segments[-1].position())


    def move(self):
        """makes it possible for the snake to move around,such that if there is three
        turtle the 3rd turtle moves to the second turtle position and the second turtle to first then
        finally first moves forward by the distance of 20"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num-1 ].xcor()
            new_y = self.segments[seg_num-1 ].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    """methods to control the movement of the snake based on the key we click"""
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.seth(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)



