'''
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:

Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true

Example 2:

Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false

Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.

'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        columns = [set() for _ in range(len(board))]
        squares = [set() for _ in range(len(board))]

        for row_idx in range(len(board)):
            for col_idx in range(len(board[row_idx])):
                # print(f'{row_idx=}, {col_idx=}')
                element = board[row_idx][col_idx]
                if element == ".":
                    continue

                if element in rows[row_idx]:
                    # print(f'{element=} is found in {rows[row_idx]=}')
                    return False

                # print(f'adding {element=} to row {row_idx=}')
                rows[row_idx].add(element)

                if element in columns[col_idx]:
                    # print(f'{element=} is found in {columns[col_idx]=}')
                    return False
                
                # print(f'adding {element=} to column {col_idx=}')
                columns[col_idx].add(element)

                square_id = (row_idx // 3) * 3 + (col_idx // 3)
                if element in squares[square_id]:
                    # print(f'{element=} is found in {squares[square_id]=}')
                    return False

                # print(f'adding {element=} to square {square_id=}')
                squares[square_id].add(element)

        return True
