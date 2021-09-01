AI = False
import os
from random import choice, randint
from asyncio import run, sleep
from sys import exit
from random import choice
from time import sleep
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
def checkhorizontal(_board, _turn):
    for row in _board:
        if len(set(row)) == 1 and list(set(row))[0] == _turn:
            return True
    return False
def checkvertical(_board, _turn):
    for i in range(0, 3):
        if _board[0][i] == _turn and _board[1][i] == _turn and _board[2][i] == _turn:
            return True
    return False
def checkdiagonal(_board, _turn):
    if _board[0][0] == _turn or _board[0][2] == _turn:
        if _board[1][1] == _turn:
            if _board[2][2] == _turn or _board[2][0] == _turn:
                return True
    return False
red = "\x1b[1;31m"
default = "\x1b[1;0m"
def format(_board):
    return f"""
      1   2   3
   1 [{_board[0][0]}] [{_board[0][1]}] [{_board[0][2]}] 
   2 [{_board[1][0]}] [{_board[1][1]}] [{_board[1][2]}] 
   3 [{_board[2][0]}] [{_board[2][1]}] [{_board[2][2]}]
    """
def cls():
    os.system("cls" if os.name == "nt" else "clear")
cls()
turn = "X"
last_turn = None
try:
    while True:
        if checkhorizontal(board, last_turn) or checkvertical(board, last_turn) or checkdiagonal(board, last_turn):
            cls()
            #print(format(board))
            #print(f"\x1b[1;31m     {last_turn} won! GG\x1b[1;0m")
            #exit(0)
            board = [
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ]
            turn = "X"
            last_turn = None
        print(format(board))
        GameOver = True
        for row in board:
            for i in row:
                if i == " ":
                    GameOver = False
        if GameOver:
            print("\x1b[1;31mGame Over! Its a tie!\x1b[1;0m")
            exit(0)
            pass
        if turn == "X" and AI == False:
            inputted = input(f"Its {turn}'s turn, pick a spot \nor type \"help\" for info on how to play\n")
        else:
            inputted = choice(["1.1", "1.2", "1.3", "2.1", "2.2", "2.3", "3.1", "3.2", "3.3"])
        il = "".join("".join(inputted.lower().split(".")).split(",")).replace(" ", "")
        try:
            il2 = int(int(il[:1]) - 1)
            il1 = int(int(il[1:]) - 1)
        except:
            pass
        if len(il) != 2:
            cls()
            print(f"{red}You have to format the spots like this: 2.2 or 2,2 or just 22{default}")
        else:
            try: il = str(int(il) - 11)
            except: pass
            if len(il) < 2:
                il = str(0 + int(il))
            if len(il) > 2:
                cls()
                print(red + "Please only insert 2 numbers" + default)
                raise KeyboardInterrupt
            if il == "help":
                cls()
                print(f"{red}Below this message is a tic tac toe map, type the values (2.2 = center and 3.3 = bottom right){default}")
            else:
                if il == '':
                    il = "00"
                if board[int(il1)][int(il2)] == " ":
                    last_turn = turn
                    board[int(il1)][int(il2)] = turn
                    turn = "O" if turn == "X" else "X"
                    cls()
                else:
                    cls()
                    print("\x1b[1;31mThat spot is already taken!\x1b[1;0m")
except (KeyboardInterrupt, EOFError):
    cls()
    print("Thanks for playing! have a good day!")
    exit(0)
