'''
You are given a 2-D matrix grid. Each cell can have one of three possible values:

    0 representing an empty cell
    1 representing a fresh fruit
    2 representing a rotten fruit

Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

Example 1:

Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

Output: 4

Example 2:

Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

Output: -1

Constraints:

    1 <= grid.length, grid[i].length <= 10

'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fruits = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    fruits.append((i, j, 0))
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        visited = set()
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        minutes = -1
        
        while fruits:
            r, c, m = fruits.popleft()
            minutes = m

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr, nc) in visited:
                    continue

                if nr in range(len(grid)) and nc in range(len(grid[0])):
                    if grid[nr][nc] == 1:
                        fruits.append((nr, nc, m + 1))
                        visited.add((nr, nc))
        
        if len(visited) < fresh:
            return -1

        return minutes






        