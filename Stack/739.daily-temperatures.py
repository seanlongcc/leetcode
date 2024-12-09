#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List

# @lc code=start


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        # iterate through the array
        for i in range(len(temperatures)):
            # check if the current element is greater than the the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # pop top of stack
                idx = stack.pop()
                # set the element at the proper index to the difference of indexes
                answer[idx] = i-idx
            # then add current index to stack
            stack.append(i)

        return answer

        # @lc code=end


Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
