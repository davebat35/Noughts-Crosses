import random
board = [[1,2,3],[4,'X',6],[7,8,9]]

def DisplayBoard(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|  ", str(board[row][col]), "  ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------"*3, "+", sep="")

noMove = 1
def EnterMove(board):
    ok = 0
    while ok != 1:
        move = input("Enter Your Move: ")
        legit = len(move) == 1 and int(move) >= 1 and int(move) <= 9
        if legit == False:
            print("This move has been rejected, please try again!")
        elif legit == True:
            move = int(move) - 1
            row = move // 3
            col = move % 3
            sgn = board[row][col]
            legit2 = sgn not in ['O', 'X']
            if legit2 == False:
                print("This move has already been taken please try again!")
            elif legit2 == True:
                board[row][col] = "O"
                DisplayBoard(board)
                ok += 1
                
    #board[row][col] = "O"
    #return DisplayBoard(board) 
    
    def makeListOfFreeFields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free.append({row:col})
    return free
    
You = "O"
Computer = "X"
def VictoryFor(board, sign):
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

def DrawMove(board):
    free = makeListOfFreeFields(board)
    ranNum = random.choice(free)
    x = next(iter(ranNum))
    y_view = ranNum.values()
    y_iterator = iter(y_view)
    y = next(y_iterator)
    board[x][y] = "X"
    return DisplayBoard(board)

DisplayBoard(board)
EnterMove(board)
finished = 0
while noMove < 8 and finished != 1:
    if noMove % 2 == 0:
        EnterMove(board)
        if VictoryFor(board, You) == 1:
            print('You Win!')
            finished += 1
        noMove += 1
    elif noMove % 2 != 0:
        DrawMove(board)
        if VictoryFor(board, Computer) == 1:
            print('Computer Wins')
            finished += 1
        noMove += 1

if noMove == 8 and finished == 0:
    print('It\'s a Draw!')
