#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List
import copy
# @lc code=start


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Placeholder for the final result
        res = [0] * len(nums)
        # pref[i] will hold product of all elements before index i
        pref = [0] * len(nums)
        # suff[i] will hold product of all elements after index i
        suff = [0] * len(nums)

        # Base cases for prefix and suffix arrays:
        # No elements before index 0, so product is 1
        # set first element to 1
        pref[0] = 1
        # No elements after the last index, so product is 1
        # set last element to 1
        suff[len(nums) - 1] = 1

        # Build prefix products:
        # After this loop, pref[i] = nums[0] * nums[1] * ... * nums[i-1]
        for i in range(1, len(nums)):
            # Multiply the previous prefix product by the element immediately before i
            pref[i] = nums[i - 1] * pref[i - 1]

        # Build suffix products:
        # After this loop, suff[i] = nums[i+1] * nums[i+2] * ... * nums[n-1]
        # Start at n - 2 since we already have n - 1 set
        for i in range(len(nums) - 2, -1, -1):
            # Multiply the next suffix product by the element immediately after i
            suff[i] = nums[i + 1] * suff[i + 1]

        # Combine prefix and suffix products to form the final result:
        # At each index i, res[i] = (product of all before i) * (product of all after i)
        for i in range(len(nums)):
            res[i] = pref[i] * suff[i]

        return res

        # OPTIMAL
        # answer = [1] * len(nums)

        # left = 1
        # for i in range(len(nums)):
        #     answer[i] = left
        #     left *= nums[i]
        # right = 1
        # for i in range(len(nums)-1, -1, -1):
        #     answer[i] *= right
        #     right *= nums[i]
        # return answer

        # O(n^2), exceeds time limit
        # answer = []
        # for i in range(len(nums)):
        #     nums_copy = copy.deepcopy(nums)
        #     nums_copy.pop(i)
        #     result = 1
        #     for num in nums_copy:
        #         result *= num
        #     answer.append(result)
        # return answer

        # @lc code=end


Solution().productExceptSelf([1, 2, 3, 4])
