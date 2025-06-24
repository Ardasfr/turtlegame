import turtle
from random import randint
import time

score = 0
sure = 100
ekran = turtle.Screen()
ekran.bgcolor("lightblue")
ekran.setup(width=600,height=600)
ekran.title("Yakalanbaç:)")
skor_yazici = turtle.Turtle()
skor_yazici.hideturtle()
skor_yazici.penup()
skor_yazici.goto(-280, 260)  # Sol üst köşe gibi
skor_yazici.write(f"Skor: {score}", font=("Arial", 16, "bold"))
zaman_yazici = turtle.Turtle()
zaman_yazici.hideturtle()
zaman_yazici.penup()
zaman_yazici.goto(180, 260)
zaman_yazici.write(f"Süre: {sure}", font=("Arial", 16, "bold"))
tosba = turtle.Turtle()
tosba.shapesize(2,2)
def update_score(x,y):
    global score
    score += 1
    skor_yazici.clear()
    skor_yazici.write(f"Skor: {score}", font=("Arial", 16, "bold"))

tosba.onclick(update_score)

for i in range(sure):
    tosba.shape("turtle")
    tosba.color("green")
    tosba.pu()
    tosba.goto(randint(-280, 280), randint(-280, 280))
    tosba.hideturtle()
    time.sleep(1)
    tosba.showturtle()
    zaman_yazici.clear()
    zaman_yazici.write(f"Süre: {sure - i}", font=("Arial", 16, "bold"))

tosba.hideturtle()
zaman_yazici.clear()
zaman_yazici.goto(0, 0)
zaman_yazici.write("Oyun Bitti!", align="center", font=("Arial", 24, "bold"))
turtle.mainloop()