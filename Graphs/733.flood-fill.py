#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# autopep8: off
# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # get the length of row and column
        # keep track of the original color

        # edge case if the original color of the source point is equal to the new color

        # create a stack, the stack represents pixel we havent checked
            # while the stack is not empty
                # pop the pixel out the stack to check
                    # check if the pixel is within the bounds
                        # check if its the original color
                        # change the pixel to the new color
                        # add all neighbors to the stack

        # return the image

        # @lc code=end
