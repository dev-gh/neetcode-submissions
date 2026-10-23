'''
You are given a m×nm×n 2D grid initialized with these three possible values:

    -1 - A water cell that can not be traversed.
    0 - A treasure chest.
    INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    grid[i][j] is one of {-1, 0, 2147483647}

'''
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647
        cells = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    cells.append((i, j))

        while cells:
            r, c = cells.popleft()
            # print(f'{r=}, {c=}, {grid[r][c]=}')

            if r > 0 and grid[r - 1][c] == land:
                grid[r - 1][c] = grid[r][c] + 1
                cells.append((r - 1, c))
            if c > 0 and grid[r][c - 1] == land:
                grid[r][c - 1] = grid[r][c] + 1
                cells.append((r, c - 1))
            if r < len(grid) - 1 and grid[r + 1][c] == land:
                grid[r + 1][c] = grid[r][c] + 1
                cells.append((r + 1, c))
            if c < len(grid[0]) - 1 and grid[r][c + 1] == land:
                grid[r][c + 1] = grid[r][c] + 1
                cells.append((r, c + 1))
            

        