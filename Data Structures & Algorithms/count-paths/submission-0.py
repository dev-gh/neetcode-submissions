'''
There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

You may assume the output will fit in a 32-bit integer.

Example 1:

Input: m = 3, n = 6

Output: 21

Example 2:

Input: m = 3, n = 3

Output: 6

Constraints:

    1 <= m, n <= 100

'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Plain combinatorics formula (but works if no other limitations e.g. blocked cells):
        C((total moves)!, (num of down)! * (num of right)!)
        
        e.g. D = 2, R = 5, so C((5+2)!, 2! * 5!) = 7! / (2! * 5!)
        
        '''       
        dp = [0] * (m * n)
        dp[0] = 1

        for i in range(1, m * n):
            row, column = divmod(i, n)

            if row == 0:
                dp[i] = 1
            elif column == 0:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + dp[i - n]

        return dp[-1]

            