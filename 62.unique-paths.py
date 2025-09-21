#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Compute the number of unique paths from the top-left to the bottom-right
        of an m x n grid when you can only move either right or down.

        Uses 1D dynamic programming with rolling updates:
        - Time:  O(m * n)
        - Space: O(n)
        """

        # `row[j]` will store the number of ways to reach the current row's cell at column `j`.
        # Initialize the first row to all 1s:
        # In the top row, you can only move right to reach any cell, so there's exactly 1 way.
        # Example for n=5: row = [1, 1, 1, 1, 1]
        row = [1] * n

        # We now iterate over the remaining m-1 rows (since the first row is already accounted for).
        # For each new row, we update `row` in-place so it becomes the count for that row.
        for i in range(0, m - 1):
            # Walk left-to-right across columns, updating the number of ways in place.
            for j in range(0, n):
                if j == 0:
                    # First column (j=0): there is only 1 way to reach any cell in the first column—
                    # you must come straight down from above. Keep it as 1.
                    row[j] = 1
                else:
                    # For other columns:
                    # Number of ways to reach (i, j) equals:
                    #   ways from above   +   ways from the left
                    # which in our rolling array is:
                    #   row[j] (old value for the same column = from above)
                    # + row[j-1] (already updated for this row = from left)
                    row[j] += row[j - 1]

                    # After this assignment, row[j] holds the correct number of paths
                    # to the cell in the current row at column j.

        # After processing all rows, the last entry corresponds to the bottom-right cell (m-1, n-1).
        return row[n - 1]

# @lc code=end
