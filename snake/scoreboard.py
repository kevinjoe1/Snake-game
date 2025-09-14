from turtle import Turtle
SCORE = 0
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

"""Creating a scoreboard class to keep track of the score"""
class Score(Turtle):
    def __init__(self):
        """score is also a turtle.Defining the characteristics of the turtle score
        special method write() transforms the turtle to a text format"""
        super().__init__()
        self.mark = 0
        with open ("data.txt") as data:
            self.highscore = int(data.read())

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        """displays the turtle and update the score"""
        self.clear()
        self.write(f"SCORE: {self.mark} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.mark > self.highscore:
            self.highscore = self.mark
            with open("data.txt",mode='w') as wdata:
                wdata.write(f"{self.highscore}")
        self.mark = 0
        self.update_score()


    """method to increase the score by 1 each time the snake collides with the food"""
    def increase_score(self):
        self.mark +=1

        self.update_score()








