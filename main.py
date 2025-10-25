from random import choice


def print_board():
    print(" ----- " * 3)
    for i in range(3):
        for j in range(3):
            if j == 1:
                print(f"|  {board[i][0]}  |"
                      f"|  {board[i][1]}  |"
                      f"|  {board[i][2]}  |")
            else:
                print("|     |" * 3)
        print(" ----- " * 3)


def is_space_taken(num):
    return space[space.index(num)] == "X" or \
        space[space.index(num)] == "O"


def space_left():
    count = 0
    for s in space:
        if s != "X" and s != "O":
            count += 1
    return count


def is_player_win(player):
    return (space[0] == player and space[1] == player and space[2] == player) or \
        (space[3] == player and space[4] == player and space[5] == player) or \
        (space[6] == player and space[7] == player and space[8] == player) or \
        (space[0] == player and space[3] == player and space[6] == player) or \
        (space[1] == player and space[4] == player and space[7] == player) or \
        (space[2] == player and space[5] == player and space[8] == player) or \
        (space[0] == player and space[4] == player and space[8] == player) or \
        (space[2] == player and space[4] == player and space[6] == player)


print("Welcome to Tic Tac Toe!")

space = [str(x + 1) for x in range(9)]
board = [space[0:3], space[3:6], space[6:9]]
end_game = False
options = ["X", "O"]
player = input("Choose X or O: ").upper()
while player not in options:
    player = input("Invalid input! Choose X or O: ").upper()
options.remove(player)
bot = options[0]
print(f"You chose {player}\n\n\n")
print(f"You: {player}")
print(f"Bot: {bot}\n\n")
print("Let the game begin!")
while not end_game:
    print_board()
    user_move = input("Choose a number from 1 to 9:")
    while not (user_move in space) or is_space_taken(user_move):
        print_board()
        user_move = input("Invalid input or number is already taken! Choose a number from 1 to 9:")
    space[space.index(user_move)] = player
    bot_move = choice(space)
    while is_space_taken(bot_move):
        bot_move = choice(space)
    space[space.index(bot_move)] = bot
    board = [space[0:3], space[3:6], space[6:9]]
    if is_player_win(bot):
        print_board()
        print("Bot wins!")
        end_game = True
    elif is_player_win(player):
        print_board()
        print("Player wins!")
        end_game = True
    elif space_left() == 1:
        print_board()
        print("It's a tie!")
        end_game = True
