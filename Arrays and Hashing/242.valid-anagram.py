#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # hash map method
    #  if len(s) != len(t):
    #         return false

    #     count_s, count_t = {}, {}

    #     for i in range(len(s)):
    #         count_s[s[i]] = 1 + count_s.get(s[i], 0)
    #         count_t[t[i]] = 1 + count_t.get(t[i], 0)
    #     return count_s == count_t

# @lc code=end
