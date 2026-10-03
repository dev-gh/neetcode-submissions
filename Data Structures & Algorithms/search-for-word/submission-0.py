'''
Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:

Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true

Example 2:

Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: false

Constraints:

    1 <= board.length, board[i].length <= 5
    1 <= word.length <= 10
    board and word consists of only lowercase and uppercase English letters.

'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        progress = []

        for i in range(len(board) * len(board[0])):
            row = i // len(board[0])
            column = i % len(board[0])

            pos = 0
            checked = set()
            if board[row][column] == word[pos]:
                checked.add((row, column))
                progress.append((pos, row, column, checked))
                while progress:
                    p, r, c, checked = progress.pop()
                    
                    if len(word) - 1 == p:
                        return True

                    p += 1
                        
                    if r > 0 and board[r - 1][c] == word[p]:
                        if (r - 1, c) not in checked:
                            new_checked = checked.copy()
                            new_checked.add((r -1, c))
                            progress.append((p, r - 1, c, new_checked))
            
                    if c > 0 and board[r][c - 1] == word[p]:
                        if (r, c - 1) not in checked:
                            new_checked = checked.copy()
                            new_checked.add((r, c - 1))
                            progress.append((p, r, c - 1, new_checked))

                    if r < len(board) - 1 and board[r + 1][c] == word[p]:
                        if (r + 1, c) not in checked:
                            new_checked = checked.copy()
                            new_checked.add((r + 1, c))
                            progress.append((p, r + 1, c, new_checked))
                        
                    if c < len(board[0]) - 1 and board[r][c + 1] == word[p]:
                        if (r, c + 1) not in checked:
                            new_checked = checked.copy()
                            new_checked.add((r,c + 1))
                            progress.append((p, r, c + 1, new_checked))

        return False



        