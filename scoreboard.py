from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.goto(-100, 200)
        self.scorescreen()
        
    def scorescreen(self):
        self.write(self.l_score, align="left", font=("Courier", "80", "normal"))
    def lef_scoreupdate(self):
        self.l_score=0
        self.write(self.l_score, align="left", font=("Courier", "80", "normal"))

    
