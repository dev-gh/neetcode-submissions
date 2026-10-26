'''
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

    Connect: A cell is connected to adjacent cells horizontally or vertically.

    Region: To form a region connect every 'O' cell. Regions can have any shape; they do not need to be squares or rectangles.

    Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.

To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

Example 1:

Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]

Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]

Explanation: The bottom 'O' region is not captured because it touches the edge of the board, so it cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

Constraints:

    1 <= board.length, board[i].length <= 200
    board[i][j] is 'X' or 'O'.

'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        check = set()

        last_row = len(board) - 1
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                check.add((0, i))
                board[0][i] = 'S'
            if board[last_row][i] == 'O':
                check.add((last_row, i))
                board[last_row][i] = 'S'
        
        last_column = len(board[0]) - 1
        for j in range(len(board)):
            if board[j][0] == 'O':
                check.add((j, 0))
                board[j][0] = 'S'
            if board[j][last_column] == 'O':
                check.add((j, last_column))
                board[j][last_column] = 'S'

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while check:
            r, c = check.pop()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr in range(len(board)) and nc in range(len(board[0])):
                    if board[nr][nc] == 'O':
                        check.add((nr, nc))
                        board[nr][nc] = 'S'
        
        for r in range(len(board)):
            for c in range (len(board[0])):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
        


            
            
        