#統計116陳秀琳
import random

def generate_board(width, height, candy_types):
    board = [[random.randint(1, candy_types) for _ in range(width)] for _ in range(height)]
    return board

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print()

def markCandies(board):
    rows, cols = len(board), len(board[0])
    to_crush = set()
    
    # Mark rows
    for r in range(rows):
        for c in range(cols - 2):
            if board[r][c] != 0 and board[r][c] == board[r][c + 1] == board[r][c + 2]:
                to_crush.update({(r, c), (r, c + 1), (r, c + 2)})
    
    # Mark columns
    for r in range(rows - 2):
        for c in range(cols):
            if board[r][c] != 0 and board[r][c] == board[r + 1][c] == board[r + 2][c]:
                to_crush.update({(r, c), (r + 1, c), (r + 2, c)})
    
    return to_crush

def crushCandies(board, to_crush):
    for r, c in to_crush:
        board[r][c] = 0

def dropCandies(board):
    rows, cols = len(board), len(board[0])
    for c in range(cols):
        wr = rows - 1
        for r in range(rows - 1, -1, -1):
            if board[r][c] != 0:
                board[wr][c] = board[r][c]
                if wr != r:
                    board[r][c] = 0
                wr -= 1

def refill_board(board, candy_types):
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 0:
                board[r][c] = random.randint(1, candy_types)

def candyCrush(board, candy_types):
    score = 0
    while True:
        to_crush = markCandies(board)
        if not to_crush:
            break
        score += len(to_crush)
        crushCandies(board, to_crush)
        dropCandies(board)
        refill_board(board, candy_types)
    
    return board, score

def switch_and_crush(board, r1, c1, r2, c2, candy_types):
    board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]
    board, score = candyCrush(board, candy_types)
    return board, score

def main():
    width = int(input("Enter the width of the board: "))
    height = int(input("Enter the height of the board: "))
    candy_types = int(input("Enter the number of candy types: "))

    board = generate_board(width, height, candy_types)
    score = 0

    while True:
        print_board(board)
        print(f"Current Score: {score}")
        try:
            r1, c1, r2, c2 = map(int, input("Enter two adjacent cells to switch (r1 c1 r2 c2): ").split())
        except ValueError:
            print("Invalid input. Please enter four integers.")
            continue

        if abs(r1 - r2) + abs(c1 - c2) != 1:
            print("Cells are not adjacent. Please try again.")
            continue

        board, gained_score = switch_and_crush(board, r1, c1, r2, c2, candy_types)
        score += gained_score

        # Check for end condition (you can define your own)
        if all(board[r][c] != 0 for r in range(height) for c in range(width)):
            print("Game over! Final Score:", score)
            break

if __name__ == "__main__":
    main()
