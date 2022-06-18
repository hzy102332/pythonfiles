import pygame, sys, random, time# 从pygame模块导入常用的函数和常量from pygame.locals import *
# 从pygame模块导入常用的函数和常量
from pygame.locals import *


# 绘制贪吃蛇
def drawSnake(snake_Body):
    for i in snake_Body:
        pygame.draw.rect(DISPLAY, WHITE, Rect(i[0], i[1], 20, 20))

# 绘制食物的位置
def drawFood(food_Position):
    pygame.draw.rect(DISPLAY, RED, Rect(food_Position[0], food_Position[1], 20, 20))

def drawScore(score):
    # 设置分数的显示颜色
    score_Surf = BASICFONT.render('%s' %(score), True, GREY)
    # 设置分数的位置
    score_Rect = score_Surf.get_rect()
    score_Rect.midtop = (320, 240)
    # 绑定以上设置到句柄
    DISPLAY.blit(score_Surf, score_Rect)

# 游戏结束并退出def GameOver():    # 设置GameOver的显示颜色    GameOver_Surf = BASICFONT.render('Game Over!', True, GREY)    # 设置GameOver的位置    GameOver_Rect = GameOver_Surf.get_rect()    GameOver_Rect.midtop = (320, 10)    # 绑定以上设置到句柄    DISPLAY.blit(GameOver_Surf, GameOver_Rect)    pygame.display.flip()    # 等待3秒    time.sleep(3)    # 退出游戏    pygame.quit()    # 退出程序    sys.exit()
def GameOver():
    # 设置GameOver的显示颜色
    GameOver_Surf = BASICFONT.render("Game Over!", True, GREY)
    # 设置GameOver的位置
    GameOver_Rect = GameOver_Surf.get_rect()
    GameOver_Rect.midtop = (320, 10)
    # 绑定以上设置到句柄
    DISPLAY.blit(GameOver_Surf, GameOver_Rect)

    pygame.display.flip()

    # 等待3秒
    time.sleep(3)
    # 退出游戏
    pygame.quit()
    # 退出程序
    sys.exit()


# 初始化Pygame库pygame.init()# 初始化一个游戏界面窗口DISPLAY = pygame.display.set_mode((640, 480))# 设置游戏窗口的标题pygame.display.set_caption('人人都是Pythonista - Snake')# 定义一个变量来控制游戏速度FPSCLOCK = pygame.time.Clock()# 初始化游戏界面内使用的字体BASICFONT = pygame.font.SysFont("SIMYOU.TTF", 80)# 定义颜色变量BLACK = pygame.Color(0, 0, 0)WHITE = pygame.Color(255, 255, 255)RED = pygame.Color(255, 0, 0)GREY = pygame.Color(150, 150, 150)
pygame.init()
# 初始化一个游戏界面窗口
DISPLAY = pygame.display.set_mode((640, 480))
# 设置游戏窗口的标题
pygame.display.set_caption('Greedy_Snake')
# 定义一个变量来控制游戏速度
FPSCLOCK = pygame.time.Clock()
# 初始化游戏界面内使用的字体
BASICFONT = pygame.font.SysFont("SIMYOU.TTF", 80)


# 定义颜色变量
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)

'''初始化贪吃蛇及食物'''# 贪吃蛇的的初始位置snake_Head = [100,100]# 初始化贪吃蛇的长度 (注：这里以20*20为一个标准小格子)snake_Body = [[80,100],[60,100],[40,100]]# 指定蛇初始前进的方向，向右direction = "right"# 给定第一枚食物的位置food_Position = [300,300]# 食物标记：0代表食物已被吃掉；1代表未被吃掉。food_flag = 1
# 贪吃蛇的的初始位置
snake_Head = [100,100]
# 初始化贪吃蛇的长度 (注：这里以20*20为一个标准小格子)
snake_Body = [[80,100],[60,100],[40,100]]
# 指定蛇初始前进的方向，向右
direction = "right"


# 给定第一枚食物的位置
food_Position = [300,300]
# 食物标记：0代表食物已被吃掉；1代表未被吃掉。
food_flag = 1
snake_Head[0] -= 20
direction = 'RIGHT'


while True:

    # 检测按键等Pygame事件for event in pygame.event.get():    if event.type == QUIT:        # 接收到退出事件后，退出程序        pygame.quit()        sys.exit()    # 判断键盘事件，用 方向键 或 wsad 来表示上下左右    elif event.type == KEYDOWN:        if (event.key == K_UP or event.key == K_w) and direction != DOWN:            direction = UP        if (event.key == K_DOWN or event.key == K_s) and direction != UP:            direction = DOWN        if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:            direction = LEFT        if (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:            direction = RIGHT
    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后，退出程序
            pygame.quit()
            sys.exit()

        # 判断键盘事件，用 方向键 或 wsad 来表示上下左右
        elif event.type == KEYDOWN:
            if (event.key == K_UP or event.key == K_w) and direction != 'DOWN':
                direction = 'UP'
            if (event.key == K_DOWN or event.key == K_s) and direction != 'UP':
                direction = 'DOWN'
            if (event.key == K_LEFT or event.key == K_a) and direction != 'RIGHT':
                direction = 'LEFT'
            if (event.key == K_RIGHT or event.key == K_d) and direction != 'LEFT':
                direction = 'RIGHT'


    # 根据键盘的输入，改变蛇的头部，进行转弯操作if direction == LEFT:    snake_Head[0] -= 20if direction == RIGHT:    snake_Head[0] += 20if direction == UP:    snake_Head[1] -= 20if direction == DOWN:    snake_Head[1] += 20# 将蛇的头部当前的位置加入到蛇身的列表中snake_Body.insert(0, list(snake_Head))
    if direction == 'LEFT':
        snake_Head[0] -= 20
    if direction == 'RIGHT':
        snake_Head[0] += 20
    if direction == 'UP':
        snake_Head[1] -= 20
    if direction == 'DOWN':
        snake_Head[1] += 20

    # 将蛇的头部当前的位置加入到蛇身的列表中
    snake_Body.insert(0, list(snake_Head))

    # 判断是否吃掉食物if snake_Head[0]==food_Position[0] and snake_Head[1]==food_Position[1]:    food_flag = 0else:    snake_Body.pop()
    if snake_Head[0]==food_Position[0] and snake_Head[1]==food_Position[1]:
        food_flag = 0
    else:
        snake_Body.pop()

    # 生成新的食物if food_flag == 0:    # 随机生成x, y    x = random.randrange(1,32)    y = random.randrange(1,24)    food_Position = [int(x*20),int(y*20)]    food_flag = 1
    if food_flag == 0:
        # 随机生成x, y
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        food_Position = [int(x*20),int(y*20)]
        food_flag = 1



    DISPLAY.fill(BLACK)# 画出贪吃蛇drawSnake(snake_Body)# 画出食物的位置drawFood(food_Position)# 打印出玩家的分数drawScore(len(snake_Body) - 3)# 刷新Pygame的显示层，贪吃蛇与食物的每一次移动，都会进行刷新显示层的操作来显示。pygame.display.flip()# 控制游戏速度FPSCLOCK.tick(7)# 画出贪吃蛇
    drawSnake(snake_Body)
    # 画出食物的位置
    drawFood(food_Position)
    # 打印出玩家的分数
    drawScore(len(snake_Body) - 3)
    # 刷新Pygame的显示层，贪吃蛇与食物的每一次移动，都会进行刷新显示层的操作来显示。
    pygame.display.flip()
    # 控制游戏速度
    FPSCLOCK.tick(7)


    # # 贪吃蛇触碰到边界
    if snake_Head[0]<0 or snake_Head[0]>620:
        GameOver()
    if snake_Head[1]<0 or snake_Head[1]>460:
        GameOver()
    # 贪吃蛇触碰到自己
    for i in snake_Body[1:]:
        if snake_Head[0]==i[0] and snake_Head[1]==i[1]:
            GameOver()