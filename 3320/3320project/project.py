import turtle
          #上0 下1 左2 右3
dic ={"gate": ["","","gatel","gater"],
    "gater": ["","gate","",""],
    "gatel": ["","gate","ab",""],
    "ab": ["ab1","gatel","",""],
    "ab1": ["ab2","ab","","b"],
    "ab2": ["","ab1","","ab3"],
    "ab3": ["","ab2","",""],
    "b": ["c","ab1","bc1",""],
    "bc1": ["","b","",""],
    "c": ["","b","",""],
    "cdr": ["cdr1","c","",""],
    "cdl": ["","c","",""],
    "cdr1": ["","cdr","",""],
    "bridge": ["cbpm","cdr1","",""],
    "cbpm": ["cbpm1","bridge","",""],
    "cbpm1": ["cbpm2","cbpm","",""],
    "cbpm2": ["subway","cbpm1","",""],
    "subway": ["cbpm3","cbpm2","",""],
    "cbpm3": ["qiuguanl","subway","",""],
    "qiuguanl": ["dom","cbpm3","qiuguangate",""],
    "qiuguangate": ["","qiuguanl","",""],
    "dom": ["dom2","qiuguanl","doml","domr"],
    "dom1": ["","dom","",""],
    "zhuxuan": ["","","",""],
    "domr": ["","dom","",""],
    "doml": ["","dom","",""],
    "dom2": ["","dom","","dom2r"],
    "dom2r": ["tenfeet","tenfeet","",""]
    "tenfeet": ["","dom2r","",""]
      }

windows = turtle.Screen()
windows.title("campus overview")
windows.setup(1200, 800 )
last = ".png"
name = "1"
# pic = dic[name][0]
turtle.bgpic(name+last)


# turtle.clear()
# turtle.penup()
# turtle.speed(10)#0-10
# turtle.color('red')

# turtle.goto(200,100)
# na = turtle.textinput('Input', 'Enter your name')
# turtle.write(na)

def up():
    global name
    pic = dic[name][0]
    if pic != "":
        name = pic
        turtle.bgpic(pic+last)
def left():
    global name
    pic = dic[name][2]
    if pic != "":
        name = pic
        turtle.bgpic(pic+last)
def right():
    global name
    pic = dic[name][3]
    if pic != "":
        name = pic
        turtle.bgpic(pic+last)
def down():
    global name
    pic = dic[name][1]
    if pic != "":
        name = pic
        turtle.bgpic(pic+last)

while True:
    turtle.onkey(up, "Up")
    turtle.onkey(down,"Down")
    turtle.onkey(left, "Left")
    turtle.onkey(right, "Right")
    # window await
    turtle.listen()
    windows.mainloop()
#     break

turtle.goto(200,100)
name = turtle.textinput('Input', 'Enter your name')
turtle.write(name)