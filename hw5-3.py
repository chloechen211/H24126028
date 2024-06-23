import random

def initialize_board(length, penalty_probability):
    board = {}
    for i in range(length):
        if random.random() < penalty_probability:
            board[i] = 'P'
        else:
            board[i] = '_'
    return board

def roll_dice():
    return random.randint(1, 6)

def move_player(position, dice_roll, board):
    new_position = position + dice_roll
    if new_position >= len(board):
        new_position = len(board) - 1
    return new_position

def print_board(board, player_positions, penalties):
    display_board = ['_' for _ in range(len(board))]
    for pos, player in player_positions.items():
        if player == 'A' and pos not in penalties:
            display_board[pos] = 'A'
        elif player == 'A' and pos in penalties:
            display_board[pos] = 'a'
        elif player == 'B' and pos not in penalties:
            display_board[pos] = 'B'
        elif player == 'B' and pos in penalties:
            display_board[pos] = 'b'
        elif player == 'X' and pos not in penalties:
            display_board[pos] = 'X'
        elif player == 'X' and pos in penalties:
            display_board[pos] = 'x'
    print(' '.join(display_board))

def game_end(board):
    end_board = ['P' if board[i] == 'P' else '_' for i in range(len(board))]
    print(' '.join(end_board))

def play_game():
    board_length = 30
    penalty_probability = 0.3
    board = initialize_board(board_length, penalty_probability)

    player_positions = {0: 'A', 1: 'B'}
    penalties = set()
    turn_penalties = {0: False, 1: False}
    
    current_player = 0
    while True:
        if turn_penalties[current_player]:
            turn_penalties[current_player] = False
        else:
            dice_roll = roll_dice()
            player_positions[current_player] = move_player(player_positions[current_player], dice_roll, board)

            if board[player_positions[current_player]] == 'P':
                penalties.add(player_positions[current_player])
                turn_penalties[current_player] = True
            else:
                penalties.discard(player_positions[current_player])

        print_board(board, player_positions, penalties)

        if player_positions[0] == board_length - 1 and player_positions[1] == board_length - 1:
            print("Both players win!")
            break
        elif player_positions[0] == board_length - 1:
            print("Player A wins!")
            break
        elif player_positions[1] == board_length - 1:
            print("Player B wins!")
            break

        current_player = 1 if current_player == 0 else 0

    game_end(board)

play_game()
