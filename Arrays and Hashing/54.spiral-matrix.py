#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Start at left corner
        # While not all visited:
        # Go right until you hit a wall
        # Go down until you hit a wall
        # Go left until you hit a wall
        # Go up until you hit a wall
        # Wall = the number 101 or out of bounds
        # When you reach an element, set it to 101
        res = []
        m, n = len(matrix), len(matrix[0])
        i, j = 0, -1

        while len(res) < m*n:
            while j+1 < n and matrix[i][j+1] != 101:
                j = j+1
                res.append(matrix[i][j])
                matrix[i][j] = 101
            while i+1 < m and matrix[i+1][j] != 101:
                i = i+1
                res.append(matrix[i][j])
                matrix[i][j] = 101
            while j-1 >= 0 and matrix[i][j-1] != 101:
                j = j-1
                res.append(matrix[i][j])
                matrix[i][j] = 101
            while i-1 >= 0 and matrix[i-1][j] != 101:
                i = i-1
                res.append(matrix[i][j])
                matrix[i][j] = 101

        return res

        # @lc code=end
