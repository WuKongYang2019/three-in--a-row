from graphics import *
import globalVar
import math
import min_max_algorithm

# p用于存放棋盘上的每个点，c中存放圆
p = [[0 for a in range(5)] for b in range(5)]
c = [[0 for a in range(5)] for b in range(5)]


def Board():
    # 创建5*5的棋盘
    global Win
    Win = GraphWin('人工智能作业：三子棋', 480, 600)
    for i in range(5):
        for j in range(5):
            p[i][j] = Point(80 + 80 * i, 80 + 80 * j)
            p[i][j].draw(Win)
    for i in range(5):
        Line(p[i][0], p[i][4]).draw(Win)
        Line(p[0][i], p[4][i]).draw(Win)


def FindWinner(temp=globalVar.chess):
    for i in range(5):
        for j in range(3):
            if temp[i][j:j + 3] == [1, 1, 1, ]:
                return 1
            elif temp[i][j:j + 3] == [-1, -1, -1, ]:
                return -1
    for i in range(3):
        for j in range(5):
            if temp[i][j] == temp[i + 1][j] == temp[i + 2][j] == 1:
                return 1
            elif temp[i][j] == temp[i + 1][j] == temp[i + 2][j] == -1:
                return -1
    for i in range(3):
        for j in range(3):
            if temp[i][j] == temp[i + 1][j + 1] == temp[i + 2][j + 2] == 1:
                return 1
            elif temp[i][j] == temp[i + 1][j + 1] == temp[i + 2][j + 2] == -1:
                return -1
    for i in range(2, 5):
        for j in range(3):
            if temp[i][j] == temp[i - 1][j + 1] == temp[i - 2][j + 2] == 1:
                return 1
            elif temp[i][j] == temp[i - 1][j + 1] == temp[i - 2][j + 2] == -1:
                return -1
    return 0


def PlayGame(turn):
    global Win
    if turn % 2 == 0:
        flag = False
        P = Win.getMouse()
        x = P.getX()
        y = P.getY()
        for i in range(5):
            for j in range(5):
                if math.sqrt(pow(x - p[i][j].getX(), 2) + pow(y - p[i][j].getY(), 2)) < 40 and globalVar.chess[i][j]== 0:
                    c[i][j] = Circle(p[i][j], 20)
                    c[i][j].draw(Win)
                    c[i][j].setFill('white')
                    globalVar.chess[i][j] = -1
                    flag = True
                    break
            if flag: break
    else:
        position = min_max_algorithm.process()
        i = position[0]
        j = position[1]
        c[i][j] = Circle(p[i][j], 20)
        c[i][j].draw(Win)
        c[i][j].setFill('black')
        globalVar.chess[i][j] = 1


def Run():
    global Win
    Board()
    turn = 1
    while 1:
        PlayGame(turn)
        turn += 1
        winner = FindWinner()
        if winner == 1:
            Text(Point(240, 500), 'Black Win').draw(Win)
            break
        if winner == -1:
            Text(Point(240, 500), 'White Win').draw(Win)
            break
    input()


if __name__ == '__main__': Run()
