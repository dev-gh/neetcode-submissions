'''
You are given an m x n 2-D integer array matrix and an integer target.

    Each row in matrix is sorted in non-decreasing order.
    The first integer of every row is greater than the last integer of the previous row.

Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true

Example 2:

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10000 <= matrix[i][j], target <= 10000

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        matrix_size = len(matrix) * len(matrix[0])
        right = matrix_size - 1

        counter = 3
        while right >= left:
            current = left + (right - left) // 2
            row = current // len(matrix[0])
            column = current % len(matrix[0])

            source = matrix[row][column]

            if source> target:
                right = current - 1
            elif source < target:
                left = current + 1
            else:
                return True

        return False