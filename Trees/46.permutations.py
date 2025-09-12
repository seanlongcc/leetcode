#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # https://www.youtube.com/watch?v=p9m2LHBW81M
        result = []

        # if base case conditions
        def backtrack(path):
            # append the result
            if len(nums) == len(path):
                result.append(path[:])
                return

            # for choice in choices
            for n in nums:
                # if violates_constraints
                if n in path:
                    continue

                # make choice
                path.append(n)
                # backtrack(updated_params)
                backtrack(path)
                # undo choice
                path.pop()

        backtrack([])
        return result
# @lc code=end
