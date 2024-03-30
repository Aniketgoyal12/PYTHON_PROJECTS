#Tic Tac Toe game 

#Define the board in the form of a list

board = ["-", "-", "-",
		"-", "-", "-",
		"-", "-", "-"]

#Define a function to print board

def print_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])
 
 
 #Define a function to edit the board as the player's desired location
 
def board_input(player):
	user_choice = int(input("Enter the position you want to mark (BETWEEN 0-8)"))
	while user_choice not in range(0,9):
		user_choice = int(input("INVALID INPUT. PLEASE ENTER A VALID POSITION"))
	if board[user_choice] == '-':
		board[user_choice] = player
	print_board()
 
 #Define a function to get the results of the game


def getresult():
    if (board[0] == board[1] == board[2] != "-") or \
	(board[3] == board[4] == board[5] != "-") or \
	(board[6] == board[7] == board[8] != "-") or \
	(board[0] == board[3] == board[6] != "-") or \
	(board[1] == board[4] == board[7] != "-") or \
	(board[2] == board[5] == board[8] != "-") or \
	(board[0] == board[4] == board[8] != "-") or \
	(board[2] == board[4] == board[6] != "-"):
        return "win"
    elif "-" not in board:
    		return "tie"
    else:
        return 'Play'
    

#Define a function for the gameplay


def gameplay():
    current_player = 'X'
    gameover = False
    while not gameover:
        board_input(current_player)
        game_result = getresult()
        if game_result == 'win':
            print(f'{current_player} wins')
            game_over = True
        elif game_result == 'tie':
            print("It's a tie")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"\
                
                
#Start the game

gameplay()
