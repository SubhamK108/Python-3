import os
import sys
os.system('clear')
board = list(range(1, 10))
def showboard():
    os.system('clear')
    print(board[0],' | ',board[1],' | ',board[2])
    print('___|_____|___')
    print('   |     |  ')
    print(board[3],' | ',board[4],' | ',board[5])
    print('___|_____|___')
    print('   |     |  ')
    print(board[6],' | ',board[7],' | ',board[8])
showboard()
def checkline(l, s1, s2, s3):
    if board[s1] == l and board[s2] == l and board[s3] == l:
        return True
def checkall(ch):
    if checkline(ch, 0, 1, 2):
        return True
    if checkline(ch, 3, 4, 5):
        return True
    if checkline(ch, 6, 7, 8):
        return True        
    if checkline(ch, 0, 3, 6):
        return True
    if checkline(ch, 1, 4, 7):
        return True
    if checkline(ch, 2, 5, 8):
        return True
    if checkline(ch, 0, 4, 8):
        return True
    if checkline(ch, 2, 4, 6):
        return True
def checkdraw():
    m = 0
    for i in range(9):
        if board[i] == 'X' or board[i] == 'O':
            m = m + 1
        if m == 9:
            print('               .....DRAW.....')
            sys.exit()
while True:
    p1 = int(input('            Turn of X : '))
    p1 -= 1
    if board[p1] != 'X' and board[p1] != 'O':
        board[p1] = 'X'
        showboard()
        if checkall('X') == True:
            print('               .....X WINS.....')
            sys.exit()
        checkdraw()
        while True:
            p2 = int(input('            Turn of O : '))
            p2 -= 1
            if board[p2] != 'X' and board[p2] != 'O':
                board[p2] = 'O'
                showboard()
                if checkall('O') == True:
                    print('               .....O WINS.....')
                    sys.exit()
                checkdraw()        
            else:
                print('               This spot is already taken !')
                continue
            break
    else:
        print('               This spot is already taken !')
        continue