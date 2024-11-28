#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0

        # this is used to keep track of state for the pointers, not to actually keep data
        seen = {}

        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right], 0)+1

            # the seen dict is used to keep track of what we have seen, not to get the length of
            while seen[s[right]] > 1:
                seen[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
        # @lc code=end


Solution().lengthOfLongestSubstring(s="bbbb")
