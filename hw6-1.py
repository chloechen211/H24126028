#統計116陳秀琳
def candyCrush(board):
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
                    to_crush.update({(r, r), (r + 1, c), (r + 2, c)})
        
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

    while True:
        to_crush = markCandies(board)
        if not to_crush:
            break
        crushCandies(board, to_crush)
        dropCandies(board)
    
    return board
