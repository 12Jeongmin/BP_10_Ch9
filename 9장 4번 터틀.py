import turtle
import random
t = turtle.Turtle()
t.shape("turtle")

def draw_square(x, y, c):
    t.up()                #사각형 그리기
    t.goto(x, y)
    t.down()
    t.color("black",c)
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.end_fill()
for c in ["yellow", "red", "purple", "blue"]:  #리스트에 저장된 색이 순서대로 표현
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    draw_square(x, y, c)
