'''
You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

Example 1:

Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]

Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

Example 2:

Input: heights = [[1],[1]]

Output: [[0,0],[1,0]]

Constraints:

    1 <= heights.length, heights[r].length <= 100
    0 <= heights[r][c] <= 1000

'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        
        for i in range(len(heights[0])):
            pacific.add((0, i))
        for k in range(len(heights)):
            pacific.add((k, 0))

        visited_p = set()
        while pacific:
            rp, cp = pacific.pop()
            visited_p.add((rp, cp))

            if rp > 0 and heights[rp - 1][cp] >= heights[rp][cp]:
                if (rp - 1, cp) not in visited_p:
                    pacific.add((rp - 1, cp))
            if rp < len(heights) - 1 and heights[rp + 1][cp] >= heights[rp][cp]:
                if (rp + 1, cp) not in visited_p:
                    pacific.add((rp + 1, cp))
            if cp > 0 and heights[rp][cp - 1] >= heights[rp][cp]:
                if (rp, cp - 1) not in visited_p:
                    pacific.add((rp, cp - 1))
            if cp < len(heights[0]) - 1 and heights[rp][cp + 1] >= heights[rp][cp]:
                if (rp, cp + 1) not in visited_p:
                    pacific.add((rp, cp + 1))

        atlantic = set()

        last_row = len(heights) - 1
        for j in range(len(heights[-1])):
            atlantic.add((last_row, j))
        for l in range(len(heights)):
            atlantic.add((l, len(heights[0]) - 1))

        visited_a = set()
        while atlantic:
            ra, ca = atlantic.pop()
            visited_a.add((ra, ca))

            if ra < len(heights) - 1 and heights[ra + 1][ca] >= heights[ra][ca]:
                if (ra + 1, ca) not in visited_a:
                    atlantic.add((ra + 1, ca))
            if ra > 0 and heights[ra - 1][ca] >= heights[ra][ca]:
                if (ra - 1, ca) not in visited_a:
                    atlantic.add((ra - 1, ca))
            if ca > 0 and heights[ra][ca - 1] >= heights[ra][ca]:
                if (ra, ca - 1) not in visited_a:
                    atlantic.add((ra, ca - 1))
            if ca < len(heights[0]) - 1 and heights[ra][ca + 1] >= heights[ra][ca]:
                if (ra, ca + 1) not in visited_a:
                    atlantic.add((ra, ca + 1))
        
        return list(visited_p & visited_a)
        