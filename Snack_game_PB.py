'''My First Game in Python'''
import turtle
import time
import random
dl=0.1

#Creating the window screen

ps=turtle.Screen()
ps.title("SNAKE GAME CREATED BY Pratyush")
ps.bgcolor("magenta")

#Dimensions of the screen

ps.setup(width=600 , height=600)
ps.tracer(0)

'''Head of the Snake'''

hd=turtle.Turtle()
hd.speed(0)
hd.shape("triangle")
hd.color("gray60")
hd.penup()
hd.goto(0,0)
hd.direction="stop"

#Points in the game(FOOD)

fd=turtle.Turtle()
fd.speed(0)
fd.shape("circle")
fd.color("gray1")
fd.penup()
fd.goto(0,90)
s=[]

#PEN 

pen=turtle.Turtle()
pen.speed(0)
pen.shape("triangle")
pen.color("beige")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

pen.write("SCORE : 0 ; HIGH SCORE : 0" , align="center" , font=("Courier",24,"normal"))

#SCORE in the game

SCORE=0
highscore=0
#FUNCTION

def right():
    if(hd.direction!= "left"):
        hd.direction="right"
def left():
    if(hd.direction!= "right"):
        hd.direction="left"
def upward():
    if(hd.direction!= "down"):
        hd.direction="up"
def downward():
    if(hd.direction!= "up"):
        hd.direction="down"
def proceed():
    if hd.direction =="right":
        x=hd.xcor()
        hd.setx(x+20)
    if hd.direction =="left":
        x=hd.xcor()
        hd.setx(x-20)
    if hd.direction =="up":
        Y=hd.ycor()
        hd.sety(Y+20)
    if hd.direction =="down":
        Y=hd.ycor()
        hd.sety(Y-20)

'''connections'''

ps.listen()
ps.onkeypress(right,"d")
ps.onkeypress(left,"a")
ps.onkeypress(upward,"w")
ps.onkeypress(downward,"s")


'''[    Main Game Loop    ]'''
while True:
    ps.update()

    #collision with boders

    if (hd.xcor()>290 or hd.xcor()< -290 or hd.ycor()>290 or hd.ycor()< -290):
        
        time.sleep(1)
        hd.goto(0,0)
        hd.direction="stop"
        for j in s:
            j.goto(1000,1000)
        
        s.clear() #Back to start point
        #Reset

        SCORE=0
        dl=0.1

        pen.clear()
        pen.write("SCORE : {} ; HIGH SCORE : {}".format(SCORE,highscore) ,align="center" , font=("Courier",24,"normal"))
    
    '''Moving the food'''
    if hd.distance(fd)<20:
        fd.goto(random.randint(-290,290),random.randint(-290,290))
        
        #SEGMENTS OF THE SNAKE
        new_s=turtle.Turtle()
        new_s.speed(0)
        new_s.shape("triangle")
        new_s.color("black")
        new_s.penup()
        s.append(new_s)

        dl-=0.0001

        SCORE+=8
        if(SCORE>highscore):
            highscore=SCORE
        
        pen.clear()
        pen.write("SCORE : {} ; HIGH SCORE : {}".format(SCORE,highscore) ,align="center" , font=("Courier",24,"normal"))
    for i in range(len(s)-1,0,-1):
        x=s[i-1].xcor()
        Y=s[i-1].ycor()
        s[i].goto(x,Y)

    if(len(s)>0):
        
        s[0].goto(hd.xcor(),hd.ycor())

    proceed()
    #Head and body collision
    for j in s:
        if (j.distance(hd)<20):
        
            time.sleep(1)
            hd.goto(0,0)
            hd.direction="stop"
            for j in s:
                j.goto(1000,1000)
        
            s.clear() #Back to start point

            #Reset
            
            SCORE=0
            dl=0.1#reset the speed

            #UPDATE
            pen.clear()
            pen.write("SCORE : {} ; HIGH SCORE : {}".format(SCORE,highscore) ,align="center" , font=("Courier",24,"normal"))
    time.sleep(dl)
ps.mainloop()