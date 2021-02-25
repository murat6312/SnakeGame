from turtle import *
import random
import time

start_time = time.perf_counter()
score_text = Turtle()
score_text.hideturtle()
wn = Screen()
wn.bgcolor("white")

passed_coords = []
screenx, screeny = 300, 300
wn.setup(screenx,screeny)
wn.screensize(int(screenx/2),int(screeny/2))

s = Turtle()
s.color("black")
s.speed(10)
s.pensize(5)

invis_snake = Turtle()
invis_snake.color("white")
invis_snake.speed(10)
invis_snake.pensize(5)
invis_snake.shape("blank")

start_counter = 0 #for invis_snake
score = 0
score_text.write("Use <- and -> to move")
nn=-2
flag = False

def length():
    global  start_counter,nn, flag
    start_counter += 1

    if flag==False:
        if start_counter>=3 :
            i = passed_coords[nn]
            invis_snake.goto(i)

    if flag==True:
        nn=nn-2

def food():
    global f
    f = Turtle(visible=False)
    fx = random.randrange(-int(screenx/2-20), int(screeny/2-20) )
    fy = random.randrange(-int(screenx/2-20), int(screeny/2-20) )
    f.penup()
    f.setpos(fx, fy)
    f.shape("circle")
    f.color("yellow")
    f.showturtle()

def eat():
    global score, flag
    a,b = s.position()
    c,d = f.position()
    flag=False
    if c-7<= a and a <=c+7 and d-7<= b and b<=d+7 :
        score +=1
        f.hideturtle()
        food()
        score_text.clear()
        score_text.write(score)
        flag = True

def game_over():
    global passed_coords, wn, nn
    a = s.position()
    a=round(a[0]),round(a[1])

    if screenx/2 <= a[0] or a[0]<= -screenx/2  or screeny/2 <= a[1] or a[1] <= -screeny/2:
        print(a)
        print("GG!!!")
        wn.bye()
    for i in passed_coords:

        if (i[0]-4<=a[0]<=i[0]+4) and \
                (i[1]-4<=a[1]<=i[1]+4):
            print(a)
            wn.bye()

    passed_coords.append(a)
    if len(passed_coords)>1-nn: #1-nn related to length() start_counter>=#
        passed_coords.pop(0)

def move_continuously():

    s.forward(10)
    eat()
    length()
    step_speed = 400+10*nn
    if step_speed<101:
        step_speed = 100
    game_over()
    ontimer(move_continuously,step_speed)

def left():
    onkeypress(None, "Left")
    s.left(90)

def right():
    onkeypress(None, "Right")
    s.right(90)

food()
move_continuously()
onkey( left,"Left")
onkey( right,"Right")
listen()
done()
end_time = time.perf_counter()
print(f"GAME OVER! You lived {int(end_time- start_time)} seconds and your score is:{score}")
