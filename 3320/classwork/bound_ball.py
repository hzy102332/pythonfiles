import turtle #导入乌龟库。Pygame
import winsound #播放声音的库

wn = turtle.Screen()
wn.title("Bound Ball Game")
wn.setup( 800 , 600 )
wn.bgcolor("black")
wn.tracer( 0 )

# 小球 ball
ball=turtle.Turtle() #turtle 模块名，Turtle 类名 实例初始化
ball.speed(0) #0最快速度，1-9级不同速度
ball.shape("circle") #shape 形状：square circle,trianle...
ball.color("white") #物品原色，默认颜色是黑色
ball.fillcolor("White")
ball.penup() #状态 抬笔
ball.dx= 0.2 #水平方向移动距离
ball.dy= 0.2 #垂直方向移动距离

# 档板A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.penup()
paddleA.goto( -350, 0 )
paddleA.shapesize( stretch_wid = 3, stretch_len = 0.5)


# 档板B
paddleB = turtle.Turtle()
paddleB.speed( 0 )
paddleB.shape("square")
paddleB.color("red")
paddleB.penup()
paddleB.goto( 350, 0 )
paddleB.shapesize( stretch_wid = 3, stretch_len = 0.5)



#计分变量
Score_A=0#玩家A的得分
Score_B=0#玩家A的得分

#游戏的计分系统
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle#隐藏画笔
pen.goto(0,-270)#中间正上方
pen.write("Right: Speed up     Left: Slow down",align="center",font=("Courier",12,'bold'))
pen.goto(0,260)#中间正上方
showText= f"玩家A得分{Score_A},玩家B得分{Score_B}"
pen.write(showText,align="center",font=("Courier",12,"bold"))


pen.hideturtle()

#定义一个函数，移动挡板向上
def paddleA_up():
    y=paddleA.ycor()#返回当前的Y坐标
    y=y+30
    if y >= 260:
        y = 260
    paddleA.sety(y)#设置当前的Y坐标

#定义一个函数，移动挡板向下
def paddleA_down():
    y=paddleA.ycor()#返回当前的Y坐标
    y=y-30
    if y <= -260:
        y = -260
    paddleA.sety(y)#设置当前的Y坐标

#定义一个函数，移动挡板向上
def paddleB_up():
    y=paddleB.ycor()#返回当前的Y坐标
    y=y+30
    if y >= 260:
        y = 260
    paddleB.sety(y)#设置当前的Y坐标

#定义一个函数，移动挡板向下
def paddleB_down():
    y=paddleB.ycor()#返回当前的Y坐标
    y=y-30
    if y <= -260:
        y = -260
    paddleB.sety(y)#设置当前的Y坐标

def ball_speed1():
    ball.dx = ball.dx * (1.2)
    ball.dy = ball.dy * (1.2)

def ball_speed2():
    ball.dx = ball.dx * (0.8)
    ball.dy = ball.dy * (0.8)

while True:


    # 玩家需要按w向上，s向下
    wn.listen() #事件侦听
    wn.onkeypress(paddleA_up,"w") #按下去的键的侦测
    wn.onkeypress(paddleA_down,"s") #按下去的键的侦测
    wn.onkeypress(paddleB_up,"Up") #按下去的键的侦测
    wn.onkeypress(paddleB_down,"Down") #按下去的键的侦测
    wn.onkeypress(ball_speed1,"Right")
    wn.onkeypress(ball_speed2, "Left")
    # wn.onkeypress(ball_speed3(), "3")

    wn.update()

# #让小球不断移动
    ball.setx( ball.xcor() + ball.dx )
    ball.sety( ball.ycor() + ball.dy )

# 最后给游戏添加一些音效，让游戏有更好的体验感。
# 注意：Bounce.wav 和 Win.wav文件需要与Python源文件在同一目录下。

    #上边界检测
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy=ball.dy*(-1)
        # winsound.PlaySound("Bounce.wav",winsound.SND_ASYNC)#播放声音

    #下边界检测,反向
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy=ball.dy*(-1)
        # winsound.PlaySound("Bounce.wav",winsound.SND_ASYNC)#播放声音

    #右边界检测
    if ball.xcor()>390:
        ball.setx(390)
        ball.dx=ball.dx*(-1)
        Score_A+=1
        pen.clear()
        pen.goto(0, -270)  # 中间正上方
        pen.write("Right: Speed up     Left: Slow down", align="center", font=("Courier", 12, 'bold'))
        pen.goto(0, 260)  # 中间正上方
        showText= f"玩家A得分{Score_A},玩家B得分{Score_B}"
        pen.write(showText,align="center",font=("Courier",12,"bold"))
        winsound.PlaySound("Win.wav",winsound.SND_ASYNC)#同步播放声音

    #左边界检测,反向
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx=ball.dx*(-1)
        Score_B+=1
        pen.clear()
        pen.goto(0, -270)  # 中间正上方
        pen.write("Right: Speed up     Left: Slow down", align="center", font=("Courier", 12, 'bold'))
        pen.goto(0, 260)  # 中间正上方
        showText= f"玩家A得分{Score_A},玩家B得分{Score_B}"
        pen.write(showText,align="center",font=("Courier",12,"bold"))
        winsound.PlaySound("Win.wav",winsound.SND_ASYNC)#播放声音

    #碰到挡板B反弹
    if (ball.xcor()< 350 and ball.xcor()>340) and (ball.ycor()< paddleB.ycor()+40 and ball.ycor()>paddleB.ycor()-40):
        ball.setx(340)
        ball.dx=ball.dx*(-1)
        winsound.PlaySound("Bounce.wav",winsound.SND_ASYNC)#播放声音

    #碰到挡板A反弹
    if (ball.xcor()>-350 and ball.xcor()<-340) and (ball.ycor()< paddleA.ycor()+40 and ball.ycor()>paddleA.ycor()-40):
        ball.setx(-340)
        ball.dx=ball.dx*(-1)
        winsound.PlaySound("Bounce.wav",winsound.SND_ASYNC)#播放声音































