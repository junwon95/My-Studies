HEIGHT = 20; WIDTH = 14; import curses; import random; import os; import datetime; blockPos = [3,WIDTH/2,0,random.randrange(0,7,1)]; next = random.randrange(0,7,1); nextB = ['---','-|_','_|-','__|','|__','[] ','_|_']; initime = datetime.datetime.now(); scr = 0; curses.initscr(); curses.curs_set(0); win = curses.newwin(HEIGHT,WIDTH,0,0); win.keypad(1); win.nodelay(1); blocks = [ [[0,-2],[0,-1],[0,0],[0,1]], [[-1,-1],[-1,0],[0,0],[0,1]], [[0,-1],[0,0],[-1,0],[-1,1]], [[0,-1],[0,0],[0,1],[-1,1]], [[-1,-1],[0,-1],[0,0],[0,1]], [[0,-1],[0,0],[1,-1],[1,0]], [[0,-1],[0,0],[0,1],[-1,0]] ]; curses.start_color(); curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN); curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_YELLOW); curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK); curses.init_pair(4, curses.COLOR_RED, curses.COLOR_RED); curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLUE); curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLUE); win.addch(0,0,' '); win.addch(0,1,'.',curses.color_pair(1)); win.addch(0,2,',',curses.color_pair(2)); win.addch(0,3,' ',curses.color_pair(3)); win.addch(0,4,'\'',curses.color_pair(4)); drawType = [win.inch(0,0),win.inch(0,1),win.inch(0,2),win.inch(0,3),win.inch(0,4)]
def hitCheck(key,d):
    for i in range(4):
        y = blockPos[0] + turnBlock(blockPos, blocks[blockPos[3]][i][0], blocks[blockPos[3]][i][1])[0]; x = blockPos[1] + turnBlock(blockPos, blocks[blockPos[3]][i][0], blocks[blockPos[3]][i][1])[1]
        if y >= HEIGHT - 1 : blockPos[0] -= d; return 1
        elif x >= WIDTH - 1 or x <= 0: moveBlock(blockPos,key,-1,initime); curses.beep();
        elif win.inch(y,x) == drawType[2]:
            if key in [curses.KEY_LEFT,curses.KEY_RIGHT,curses.KEY_DOWN,curses.KEY_UP]: moveBlock(blockPos,key,-1,initime); return 1 if key == curses.KEY_DOWN else curses.beep();
            else: blockPos[0] -= 1; return 1
def drawBlock(blockPos,type):
    mark = '.' if type == 1 else ',' if type == 2 else ' '
    for i in range(4): win.addch(blockPos[0] + turnBlock(blockPos, blocks[blockPos[3]][i][0], blocks[blockPos[3]][i][1])[0],
    blockPos[1] + turnBlock(blockPos, blocks[blockPos[3]][i][0], blocks[blockPos[3]][i][1])[1], mark, curses.color_pair(type))
    win.addch(0,3,' ',curses.color_pair(3));
    for i in range(4):
        for j in range(1,HEIGHT - blockPos[0]) :
            if win.inch(blockPos[0] + turnBlock(blockPos, blocks[blockPos[3]][i][0], blocks[blockPos[3]][i][1])[0] + j, blockPos[1] + turnBlock(blockPos, blocks[blockPos[3]][i][0], blocks[blockPos[3]][i][1])[1]) == drawType[0] or win.inch(blockPos[0] + turnBlock(blockPos, blocks[blockPos[3]][i][0], blocks[blockPos[3]][i][1])[0] + j, blockPos[1] + turnBlock(blockPos, blocks[blockPos[3]][i][0], blocks[blockPos[3]][i][1])[1]) == drawType[3] : win.addch('\'', curses.color_pair(4))
            else : break
def moveBlock(blockPos,key,d,init):
    if d and (60 + now.second - init.second) % 60 >= 1 : blockPos[0] += d; global initime; initime = datetime.datetime.now();
    blockPos[1] = blockPos[1] - d if key == curses.KEY_LEFT else blockPos[1] + d if key == curses.KEY_RIGHT else blockPos[1]; blockPos[0] = blockPos[0] + d if key == curses.KEY_DOWN else blockPos[0];
    if key == curses.KEY_UP : blockPos[2] = (blockPos[2] + 1) % 4 if not d == -1 else (blockPos[2] + 3) % 4
def turnBlock(blockPos,y,x): sin = [0,1,0,-1]; cos = [1,0,-1,0]; return [y,x] if blockPos[3] == 5 else [y * cos[blockPos[2]] - x * sin[blockPos[2]], y * sin[blockPos[2]] + x * cos[blockPos[2]]]
def lineClr():
    for y in range(2,HEIGHT-1):
        if all(win.inch(y,x) == drawType[2] for x in range(1,WIDTH-1)): win.deleteln(); win.move(2,1); win.insertln(); curses.beep(); curses.flash(); global scr; scr += 1
def sweep():
    for y in range(2,HEIGHT-1):
        for x in range(1,WIDTH-1):
            if win.inch(y,x) == drawType[4]: win.addch(y,x,' ',curses.color_pair(3))
while 1:
    lineClr(); win.attrset(curses.color_pair(5)); win.border('|','|','-','-','+','+','+','+'); win.addstr(0,WIDTH/2-4,'[TETRIS]', curses.color_pair(6)); win.addstr(1,WIDTH/2-6,' NEXT : '+nextB[next]+' ',curses.color_pair(6)); win.addstr(HEIGHT-1,WIDTH/2-4,'SCORE: '+str(scr), curses.color_pair(6)); now = datetime.datetime.now(); key = win.getch(); drawBlock(blockPos,3); moveBlock(blockPos,key,1,initime)
    if hitCheck(key,1): drawBlock(blockPos,2); blockPos = [2,WIDTH/2,0,next]; next = random.randrange(0,7,1);
    if hitCheck(key,0): break
    sweep(); drawBlock(blockPos,1)
win.keypad(0); win.nodelay(0); curses.endwin(); print ('\n'+'+'*(WIDTH/2-3)+'GAME OVER'+'+'*(WIDTH/2-3)+'\n'+'='*(WIDTH/2-5)+'|YOUR SCORE : '+str(scr)+'|'+'='*(WIDTH/2-5))
