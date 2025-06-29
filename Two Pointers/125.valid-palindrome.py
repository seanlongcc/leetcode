#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ''.join(filter(str.isalnum, s)).lower()

        left = 0
        right = len(alphanumeric) - 1

        while left < right:
            if alphanumeric[left] == alphanumeric[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

        # @lc code=end


Solution().isPalindrome("aa")
