import curses; import random; import os; import datetime
blockPos = [2,7,0,random.randrange(0,7,1)]; next = random.randrange(0,7,1); nextB = ['---','-|_','_|-','__|','|__','[ ]','_|_'];
initime = datetime.datetime.now(); scr = 0
curses.initscr(); curses.curs_set(0); win = curses.newwin(15,14,0,0); win.keypad(1); win.nodelay(1)
curses.start_color(); curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN); curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_YELLOW);

blocks = [
    [[0,-2],[0,-1],[0,0],[0,1]], #----
    [[-1,-1],[-1,0],[0,0],[0,1]], #-_
    [[0,-1],[0,0],[-1,0],[-1,1]], #_-
    [[0,-1],[0,0],[0,1],[-1,1]], #__|
    [[-1,-1],[0,-1],[0,0],[0,1]], #|__
    [[0,-1],[0,0],[1,-1],[1,0]], #[]
    [[0,-1],[0,0],[0,1],[-1,0]]  #_|_
]
def hitCheck(key,d) :
    win.addch(0,0,'.',curses.color_pair(2))
    for i in range(4):
        y = blockPos[0] + turnBlock(blockPos, blocks[blockPos[3]][i][0], blocks[blockPos[3]][i][1])[0]; x = blockPos[1] + turnBlock(blockPos, blocks[blockPos[3]][i][0], blocks[blockPos[3]][i][1])[1]
        if y >= 13 : blockPos[0] -= d; return 1
        elif x >= 13 : blockPos[1] -= d; curses.beep();
        elif x <= 0 : blockPos[1] += d; curses.beep();
        elif win.inch(y,x) == win.inch(0,0):
            curses.flash();
            if key in [curses.KEY_LEFT,curses.KEY_RIGHT,curses.KEY_DOWN,curses.KEY_UP]: moveBlock(blockPos,key,-1); return 1 if key == curses.KEY_DOWN else curses.beep();
            else: blockPos[0] -= 1; return 1
def drawBlock(blockPos,type):
    if type == 1 : mark = ','
    elif type == 2 : mark = '.'
    else : mark = ' '
    for i in range(4):
        win.addstr(blockPos[0] + turnBlock(blockPos, blocks[blockPos[3]][i][0], blocks[blockPos[3]][i][1])[0],
        blockPos[1] + turnBlock(blockPos, blocks[blockPos[3]][i][0], blocks[blockPos[3]][i][1])[1], mark, curses.color_pair(type))
def moveBlock(blockPos,key,d) :
    global initime;
    if d == 1 and (60 + now.second - initime.second) % 60 >= 1 : blockPos[0] += d; initime = datetime.datetime.now()
    if key == curses.KEY_LEFT : blockPos[1] -= d;
    elif key == curses.KEY_RIGHT : blockPos[1] += d
    elif key == curses.KEY_DOWN : blockPos[0] += d
    elif key == curses.KEY_UP :
        if d == 1: blockPos[2] = (blockPos[2] + 1) % 4
        else: blockPos[2] = (blockPos[2] + 3) % 4
def turnBlock(blockPos,y,x) :
    sin = [0,1,0,-1]; cos = [1,0,-1,0]
    if blockPos[3] == 5: return [y,x]
    return [y * cos[blockPos[2]] - x * sin[blockPos[2]], y * sin[blockPos[2]] + x * cos[blockPos[2]]]
def lineClr():
    win.addch(0,0,'.',curses.color_pair(2))
    for y in range(14):
        if all(win.inch(y,x) == win.inch(0,0) for x in range(1,13)):
            win.move(y,0); win.deleteln(); win.move(3,1); win.insertln(); curses.beep(); curses.flash(); global scr; scr += 1
'''
---------------<gameRun>-----------------
'''
while 1:
    lineClr()
    win.border('|','|','-','-','+','+','+','+'); win.addstr(0,3,'[TETRIS]')
    win.addstr(1,2,'NEXT : '+nextB[next]); win.addstr(2,1,'============'); win.addstr(13,1,'============|+--SCORE: '+str(scr))
    now = datetime.datetime.now(); key = win.getch()
    drawBlock(blockPos,3)
    moveBlock(blockPos,key,1)
    if hitCheck(key,1):
        drawBlock(blockPos,2)
        blockPos = [2,7,0,next]
        next = random.randrange(0,7,1)
        if hitCheck(key,0): break
    drawBlock(blockPos,1)
win.keypad(0); win.nodelay(0); curses.endwin()
print '\n+++++GAME OVER+++++\n==|YOUR SCORE : '+str(scr)+'|=='
