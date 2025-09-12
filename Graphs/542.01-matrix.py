#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # directions for moving up, left, down, right
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        # get matrix dimensions
        rows, cols = len(mat), len(mat[0])
        # intialize a queue
        queue = collections.deque()
        # create array for seen values
        seen = [[False] * cols for _ in range(rows)]

        # go through the matrix to find all the 0s
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    seen[i][j] = True

        while queue:
            i, j = queue.popleft()
            # explore the neighboring cells in all 4 directions
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                # out of bounds check
                if x < 0 or x == rows or y < 0 or y == cols:
                    continue
                # check if seen already
                if seen[x][y]:
                    continue
                # add +1 to matrix
                mat[x][y] = mat[i][j] + 1
                # then add it back to the end of the queue
                queue.append((x, y))
                seen[x][y] = True

        return mat
# @lc code=end
