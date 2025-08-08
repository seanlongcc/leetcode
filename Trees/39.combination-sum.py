#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Helper function to perform depth-first search for combinations
        def backtrack(index: int, current_sum: int):
            # Check if the current combination equals target sum
            if current_sum == 0:
                # If current sum is zero, we found a valid combination, add it to the answer list
                # stores a slice copy, if we just do it without the slice or a .copy(), it stores the reference and can be overwritten
                combinations.append(combination_so_far[:])
                return

            # If we've reached the end of candidates array, so theres nothing else to explore
            # or current_sum is less than the candidate at the index, so its not possible, stop exploring this path
            if index >= len(candidates) or current_sum < candidates[index]:
                return

            # Recurse without including the current candidate
            backtrack(index + 1, current_sum)

            # Choose the current candidate
            combination_so_far.append(candidates[index])

            # Recurse including the current candidate
            backtrack(index, current_sum - candidates[index])

            # Backtrack by removing the current candidate
            combination_so_far.pop()

        # Sort the candidates to help with early stopping in backtrack
        candidates.sort()

        # This is a temporary list to hold the current combination
        combination_so_far = []

        # This is the list to hold all unique combinations that sum up to target
        combinations = []

        # Start the backtrack from the first candidate with the summation equal to target
        backtrack(0, target)

        # Return all unique combinations found
        return combinations

        # @lc code=end
