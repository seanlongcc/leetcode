#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        # directions: right, down, left, up
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def backtrack(row: int, col: int, index: int) -> bool:
            # all chars matched
            if index == len(word):
                return True

            # out of bounds or mismatch, check if the char is # as well
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]:
                return False

            # choose: mark current cell as visited (sentinel)
            character = board[row][col]
            board[row][col] = "#"  # any non-letter sentinel works

            # explore neighbors
            # for choice in choices
            for direction_row, direction_col in directions:
                new_row, new_col = row + direction_row, col + direction_col
                if backtrack(new_row, new_col, index + 1):
                    # restore before returning
                    board[row][col] = character
                    return True

            # un-choose: restore cell for other paths
            board[row][col] = character
            return False

        # try starting from every cell that matches the first char
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True

        return False

# @lc code=end
