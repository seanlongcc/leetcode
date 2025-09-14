#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # result = []

        # # index is the index of the number we are currently deciding on
        # # path is is the current subset we are building
        # def backtrack(index, path):
        #     # base case, runs last, means we've considered every possible number
        #     # it hits it because in the previous loop to get here it does index +1
        #     # so given [1,2,3], it hits base case given index = 3
        #     if index == len(nums):
        #         # append copy of path to answer array
        #         result.append(path[:])
        #         return

        #     # decision 1: include current number (nums[index]) in the subset
        #     path.append(nums[index])
        #     # then we move on to the next number by doing index + 1
        #     backtrack(index + 1, path)
        #     # backtracking part, undoing the last number to try the other option
        #     path.pop()

        #     # decision 2: skip nums[index] without adding it to path
        #     backtrack(index + 1, path)

        # backtrack(0, [])
        # return result

        result, path = [], []

        def backtrack(start):                      # params
            # base_case_condition → for subsets we record every prefix
            result.append(path[:])

            # choices = indices we can still take
            for i in range(start, len(nums)):
                # if violates_constraints: continue   # (none for subsets)

                # make_choice
                path.append(nums[i])

                # explore
                backtrack(i + 1)                    # updated_params

                # undo_choice (backtrack step)
                path.pop()

        backtrack(0)
        return result

        # @lc code=end
