# + - head
# - - body
# = - apple
#install keyboard module before running
from time import sleep
from os import system
from random import randint
import keyboard
ma = (7, 5)
class Snake:
    direc = [1, 0]
    head = [3, 2]
    body = []
    score = 0
    def startAgain(self):
        self.head = [3, 2]
        self.direc = [1, 0]
        self.body = []
        self.score = 0
    def addBody(self):
        x, y = 0, 0
        if len(self.body) == 0:
            x = self.head[0] - self.direc[0]
            y = self.head[1] - self.direc[1]
        elif len(self.body) == 1:
            x = self.body[0][0] - (self.head[0] - self.body[0][0])
            y = self.body[0][1] - (self.head[1] - self.body[0][1])
        else:
            x = self.body[-1][0] - (self.body[-2][0] - self.body[-1][0])
            y = self.body[-1][1] - (self.body[-2][1] - self.body[-1][1])
        self.body.append([x, y])
    def move(self, direc):
        for i in range(len(self.body) - 1, -1, -1):
            if i != 0:
                self.body[i] = self.body[i - 1].copy()
            else:
                self.body[i] = self.head.copy()
            self.body[i][0] %= ma[0]
            self.body[i][1] %= ma[1]
        self.head[0] = (self.head[0] + direc[0]) % ma[0]
        self.head[1] = (self.head[1] + direc[1]) % ma[1]
    def dirChange(self, x, y):
        self.direc = [x, y]
    def headCheck(self, apple):
        if self.head in self.body:
            return True
        if apple.pos == self.head:
            self.score += 1
            apple.spawn()
        return False
snake = Snake()
class Apple:
    pos = [0, 0]
    def spawn(self):
        snake.addBody()
        while self.pos in snake.body or self.pos == [snake.head[0] % ma[0], snake.head[1] % ma[1]]:
            self.pos = [randint(0, ma[0] - 1), randint(0, ma[1] - 1)]
apple = Apple()
def drawFrame(lenx, leny):
    frame = ""
    for i in range(leny):
        for j in range(lenx):
            if [j, i] == snake.head:
                frame += "#"
            elif [j, i] == apple.pos:
                frame += "="
            elif [j, i] in snake.body:
                frame += "+"
            else:
                frame += " "
        frame += "\n"
    print(frame + "_" * lenx, snake.score)
x = 1
keyboard.add_hotkey('right', lambda: snake.dirChange(1, 0))
keyboard.add_hotkey('left', lambda: snake.dirChange(-1, 0))
keyboard.add_hotkey('up', lambda: snake.dirChange(0, -1))
keyboard.add_hotkey('down', lambda: snake.dirChange(0, 1))
while True:
    snake.startAgain()
    while not snake.headCheck(apple):
        snake.move(snake.direc)
        drawFrame(ma[0], ma[1])
        sleep(1)
    print(f"Game Over!Your score {snake.score} \nPress enter to start new game...")
    input()
    system('cls')
