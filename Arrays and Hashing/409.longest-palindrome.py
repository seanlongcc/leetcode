#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
from collections import Counter
# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        unpaired = set()

        for char in s:
            if char in unpaired:
                unpaired.remove(char)
                length += 2
            else:
                unpaired.add(char)

        if len(unpaired) > 0:
            return length + 1
        else:
            return length

            # @lc code=end
Solution().longestPalindrome(s="abccccdd")
