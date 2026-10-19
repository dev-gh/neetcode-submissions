'''
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:

Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

Example 2:

Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4

Constraints:

    1 <= grid.length, grid[i].length <= 100
    grid[i][j] is '0' or '1'.



Topics


Recommended Time & Space Complexity

You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the grid.

'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = len(grid) * len(grid[0])
        islands = 0

        for i in range(total):
            row = i // len(grid[0])
            column = i % len(grid[0])

            if grid[row][column] == '1':
                islands += 1

                tmp = set()
                tmp.add((row, column))

                while tmp:
                    r, c = tmp.pop()
                    grid[r][c] = '2'
    
                    if r > 0 and grid[r - 1][c] == '1':
                        tmp.add((r - 1, c))
                    if c > 0 and grid[r][c - 1] == '1':
                        tmp.add((r, c - 1))
                    if r < len(grid) - 1 and grid[r + 1][c] == '1':
                        tmp.add((r + 1, c))
                    if c < len(grid[0]) - 1 and grid[r][c + 1] == '1':
                        tmp.add((r, c + 1))

        return islands


                


        