import copy
import Main

import globalVar


def Findscore(temp):
    blackScore = 0
    temp1 = copy.deepcopy(temp)
    temp2 = copy.deepcopy(temp)
    for i in range(5):
        for j in range(5):
            if temp2[i][j] == 0:
                temp2[i][j] = 1
            if temp1[i][j] == 0:
                temp1[i][j] = -1
    for i in range(5):
        for j in range(3):
            if temp2[i][j:j + 3] == [1, 1, 1, ]:
                blackScore += 1
            elif temp1[i][j:j + 3] == [-1, -1, -1, ]:
                blackScore -= 5
    for i in range(3):
        for j in range(5):
            if temp2[i][j] == temp2[i + 1][j] == temp2[i + 2][j] == 1:
                blackScore += 1
            elif temp1[i][j] == temp1[i + 1][j] == temp1[i + 2][j] == -1:
                blackScore -= 5
    for i in range(3):
        for j in range(3):
            if temp2[i][j] == temp2[i + 1][j + 1] == temp2[i + 2][j + 2] == 1:
                blackScore += 1
            elif temp1[i][j] == temp1[i + 1][j + 1] == temp1[i + 2][j + 2] == -1:
                blackScore -= 5
    for i in range(2, 5):
        for j in range(3):
            if temp2[i][j] == temp2[i - 1][j + 1] == temp2[i - 2][j + 2] == 1:
                blackScore += 1
            elif temp1[i][j] == temp1[i - 1][j + 1] == temp1[i - 2][j + 2] == -1:
                blackScore -= 5
    return blackScore


def minmax(temp, player, nextplayer, deep, alpha=float('-inf'), beta=float('inf')):
    if Main.FindWinner(temp) == 1:
        return float('inf')
    elif Main.FindWinner(temp) == -1:
        return float('-inf')
    # 遍历最大深度为2
    if deep >= 2:
        return Findscore(temp)
    for i in range(5):
        for j in range(5):
            if temp[i][j] == 0:
                temp[i][j] = player
                score = minmax(temp, nextplayer, player, deep + 1, alpha, beta)
                temp[i][j] = 0
                # 更新alpha和beta
                if player == 1:
                    if score > alpha: alpha = score
                    if alpha >= beta: return alpha  # 剪枝
                else:
                    if score < beta:
                        beta = score
                    if alpha >= beta: return beta
    if player == 1:
        return alpha
    else:
        return beta


def process():
    temp = copy.deepcopy(globalVar.chess)
    score = {}
    for i in range(5):
        for j in range(5):
            if temp[i][j] == 0:
                temp[i][j] = 1
                score[(i, j)] = minmax(temp, -1, 1, 1)  # 1代表电脑，-1代表人
                temp[i][j] = 0
    return max(score.items(), key=lambda x: x[1])[0]
