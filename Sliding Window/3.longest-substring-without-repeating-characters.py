#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        # left and right are pointers
        left = 0

        # this is used to keep track of state for the pointers, not to actually keep data
        seen = {}

        # start iterating by the length of the string
        for right in range(len(s)):
            # add to the seen dict
            seen[s[right]] = seen.get(s[right], 0)+1

            # the seen dict is used to keep track of what we have seen, not to get the length of
            while seen[s[right]] > 1:
                # we dont need to delete keys like we do in Fruits into Baksets since we arent checking the length of the hash map itself ever, so its harmless
                # cant do seen[s[right]] since the indexes wont be the same char, for a counter example just look at pwwkew, the back to back w messes it up
                seen[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
        # @lc code=end


Solution().lengthOfLongestSubstring(s="bbbb")
