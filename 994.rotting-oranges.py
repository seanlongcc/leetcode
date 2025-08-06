#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # directions for moving up, down, left, right
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # get matrix dimensions
        rows, cols = len(grid), len(grid[0])
        # Initialize a queue for BFS, counter for fresh oranges, and the minutes passed
        queue = deque()
        minutes_passed = 0
        fresh_count = 0

        # Go through each cell in the grid.
        for i in range(rows):
            for j in range(cols):
                # If we find a rotten orange, add its position to the queue.
                if grid[i][j] == 2:
                    queue.append((i, j))
                # If it's a fresh orange, increment the fresh_count.
                elif grid[i][j] == 1:
                    fresh_count += 1

        # Perform BFS until the queue is empty or there are no fresh oranges left.
        while queue and fresh_count > 0:
            # Increment minutes each time we start a new round of BFS.
            minutes_passed += 1
            # Loop over all the rotten oranges at the current minute.
            for _ in range(len(queue)):
                i, j = queue.popleft()
                # Check the adjacent cells in all four directions.
                for delta_row, delta_col in directions:
                    x, y = i + delta_row, j + delta_col
                    # Out of bounds check and if the adjacent cell has a fresh orange, rot it.
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        fresh_count -= 1
                        grid[x][y] = 2
                        # Add the next orange that rots
                        queue.append((x, y))

        # If there are no fresh oranges left, return the minutes passed.
        # Otherwise, return -1 because some oranges will never rot.
        if fresh_count == 0:
            return minutes_passed
        else:
            return -1

# @lc code=end
