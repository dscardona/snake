from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.update_score()