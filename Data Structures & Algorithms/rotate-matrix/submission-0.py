'''
Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

Example 1:

Input: matrix = [
  [1,2],
  [3,4]
]

Output: [
  [3,1],
  [4,2]
]

Example 2:

Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        layers = n // 2

        for l in range(layers):
            for i in range(l, n - 1 - l):
                # top = matrix[l][i]
                # right = matrix[i][n - 1 - l]
                # bottom = matrix[n - 1 - l][n - 1 - i]
                # left = matrix[n - 1 - i][l]

                matrix[l][i], matrix[i][n - 1 - l], matrix[n - 1 - l][n - 1 - i], matrix[n - 1 - i][l] = matrix[n - 1 - i][l], matrix[l][i], matrix[i][n - 1 - l], matrix[n - 1 - l][n - 1 - i]


       