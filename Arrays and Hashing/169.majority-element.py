#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from collections import Counter
# @lc code=start


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # my hashmap method
        # majority = len(nums)/2
        # majority_element = nums[0]

        # freq = Counter(nums)
        # for char, count in freq.items():
        #     if count > majority:
        #         majority_element = char

        # return majority_element

        # OR THIS
        # freq = Counter(nums)
        # return max(freq, key=freq.get)

        # THIS SOLUTION IS O(1) SPACE
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                # pick a new candidate when count drops to zero
                candidate = num
                count = 1
            elif num == candidate:
                # increment if same as candidate
                count += 1
            else:
                # decrement otherwise
                count -= 1

        # candidate is guaranteed to be the majority element
        return candidate
        # @lc code=end


Solution().majorityElement(nums=[2, 2, 1, 1, 1, 2, 2])
