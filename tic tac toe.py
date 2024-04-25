from random import randrange

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    global user_move
    user_move = int(input("Your move! "))
    while user_move not in matrix_positions.keys():
        user_move = int(input("Not a valid move, try again "))
    position = matrix_positions[user_move]
    exec(position + "= 'x'")
    return board
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields_user(board):
    del matrix_positions[user_move]
    return matrix_positions
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
def make_list_of_free_fields_comp(board):
    del matrix_positions[computer_move]
    return matrix_positions

def victory_for(board, sign):
    for i in range(3):
        if board[i] == [sign,sign,sign]:
            print("Victory for ",sign,"!!!")
            exit()
        elif [row[i:i+1] for row in board] == [[sign],[sign],[sign]]:
            print("Victory for ",sign,"!!!")
            exit()
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        print("Victory for ",sign,"!!!")
        exit()
    if board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        print("Victory for ",sign,"!!!")
        exit()
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    global computer_move
    computer_move = randrange(9)
    while computer_move not in matrix_positions.keys():
        computer_move = randrange(9)
    print("My move! ",computer_move)
    position = matrix_positions[computer_move]
    exec(position + "= 'o'")
    return board
    # The function draws the computer's move and updates the board.

board = [[1,2,3],
         [4,5,6],
         [7,8,9]]
         
matrix_positions = {1:"board[0][0]",
                    2:"board[0][1]",
                    3:"board[0][2]",
                    4:"board[1][0]",
                    5:"board[1][1]",
                    6:"board[1][2]",
                    7:"board[2][0]",
                    8:"board[2][1]",
                    9:"board[2][2]",}

while len(matrix_positions) > 0:                    
    display_board(board)
    board = enter_move(board)
    matrix_positions = make_list_of_free_fields_user(board)
    victory_for(board,"x")
    display_board(board)
    board = draw_move(board)
    matrix_positions = make_list_of_free_fields_comp(board)
    victory_for(board,"o")