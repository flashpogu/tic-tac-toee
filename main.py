def sum(a, b, c):
    return a + b + c


def print_board(xState, yState):
    """This function will print the board while changing
     it's value of cell in the iteration unless match is over."""
    if xState[0]:
        one = "X"
    else:
        if yState[0]:
            one = "O"
        else:
            one = 1

    if xState[1]:
        two = "X"
    else:
        if yState[1]:
            two = "O"
        else:
            two = 2

    if xState[2]:
        three = "X"
    else:
        if yState[2]:
            three = "O"
        else:
            three = 3

    if xState[3]:
        four = "X"
    else:
        if yState[3]:
            four = "O"
        else:
            four = 4

    if xState[4]:
        five = "X"
    else:
        if yState[4]:
            five = "O"
        else:
            five = 5

    if xState[5]:
        six = "X"
    else:
        if yState[5]:
            six = "O"
        else:
            six = 6

    if xState[6]:
        seven = "X"
    else:
        if yState[6]:
            seven = "O"
        else:
            seven = 7

    if xState[7]:
        eight = "X"
    else:
        if yState[7]:
            eight = "O"
        else:
            eight = 8

    if xState[8]:
        nine = "X"
    else:
        if yState[8]:
            nine = "O"
        else:
            nine = 9

    print(f"{one} | {two} | {three} ")
    print(f"__|___|___")
    print(f"{four} | {five} | {six}")
    print(f"__|___|___")
    print(f"{seven} | {eight} | {nine} ")


def check_match(xState, yState):
    """This function will check for straight line so that we can check for winner"""
    wins = [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8],\
        [2, 4, 6]  # This is array of indexes of each cell that will form the straight line.
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X won the match!")
            return 1
        if sum(yState[win[0]], yState[win[1]], yState[win[2]]) == 3:
            print("O won the match!")
            return 0
    return -1


# Both Array that will take the value of each cell, initially,
# all the cell have falsy value


xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

turn = 1  # 1 for X and 0 for O

print("Welcome to Tic Tac Toe\n")

while True:
    print_board(xState, yState)
    if turn == 1:
        print("X's Chance")
        value = int(input("Please enter a value: "))
        xState[value-1] = 1  # it will input the value in array in relative position
    else:
        print("O's Chance")
        value = int(input("Please enter a value: "))
        yState[value-1] = 1
    winner = check_match(xState, yState)  # it will check for the winner
    if winner != -1:
        break
    turn = 1 - turn  # it will change the turn with one end of iteration



