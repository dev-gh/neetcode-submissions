'''
You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.

Example 1:

Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

Output: 6

Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.

Constraints:

    1 <= grid.length, grid[i].length <= 50



Topics


Recommended Time & Space Complexity

You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the grid.

'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        visited = set()

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                # print(f'{row=}, {column=}')
                if (row, column) in visited:
                    # print(f'skipped {row=}, {column=}')
                    continue

                if grid[row][column] == 1:
                    # print(f'land')
                    before = len(visited)
                    island = set()
                    island.add((row, column))

                    while island:
                        r, c = island.pop()
                        # print(f'checking {r=}, {c=}')
                        visited.add((r, c))

                        if r > 0 and grid[r - 1][c] == 1:
                            if (r - 1, c) not in visited:
                                island.add((r - 1, c))
                        if c > 0 and grid[r][c - 1] == 1:
                            if (r, c - 1) not in visited:
                                island.add((r, c - 1))
                        if r < len(grid) - 1 and grid[r + 1][c] == 1:
                            if (r + 1, c) not in visited:
                                island.add((r + 1, c))
                        if c < len(grid[0]) - 1 and grid[r][c + 1] == 1:
                            if (r, c + 1) not in visited:
                                island.add((r, c + 1))
                        
                    # print(f'{area=}, {len(visited)=}, {before=}')
                    area = max(area, len(visited) - before)

        return area
        