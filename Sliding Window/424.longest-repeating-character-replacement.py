#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # in this problem, we dont actually change letters, but instead use the length of the window to check validity
        seen = {}
        max_freq = 0
        max_length = 0
        left = 0

        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right], 0) + 1

            # we get the max frequency to determine which of the letter in the window we "change" the other letter into
            max_freq = max(max_freq, seen[s[right]])

            # if the current sliding window exceeds the limit, then we shrink the window
            # its checking if we still have enough letters to change or if we have hit the limit
            if right - left + 1 > k + max_freq:
                seen[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

        # @lc code=end


Solution().characterReplacement(s="ABAB", k=2)
