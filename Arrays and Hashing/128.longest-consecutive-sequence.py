#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

from typing import List
# @lc code=start

# the key is to look at previous element instead of next element


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n-1) not in num_set:
                length = 0
                while (n+length) in num_set:
                    length += 1
                longest = max(length, longest)

        return longest

        # if not nums:
        #     return 0

        # nums.sort()

        # max_length = 1
        # current_length = 1

        # for i in range(1, len(nums)):
        #     # compare to previous element to skip duplicates
        #     if nums[i] == nums[i - 1]:
        #         continue
        #     # Checks if the current number is exactly one greater than the previous number
        #     elif nums[i] == nums[i - 1] + 1:
        #         current_length += 1
        #     # Sequence breaks, update max_length and reset current_length
        #     else:
        #         max_length = max(max_length, current_length)
        #         current_length = 1

        # Return the maximum length (considering the last sequence)
        # print(max(max_length, current_length))
        # return max(max_length, current_length)

        # @lc code=end


Solution().longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6])
