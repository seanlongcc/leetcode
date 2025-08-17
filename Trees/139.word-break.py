#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # THIS FOLLOWS THE BACKTRACKING TEMPLATE

        # add cache so that the time complexity passes
        cache = {}

        def backtrack(s):
            # first check the cache
            if s in cache:
                return cache[s]

            # Base case: empty remainder means we've successfully segmented all chars.
            if s == "":
                cache[s] = True
                return True

            # check if the prefix is in the word
            for word in wordDict:
                # only proceed if the current string starts with the word
                if not s.startswith(word):
                    continue

                # if the word exists, chop off the existing word to create a new string
                s = s[len(word):]
                # need to be an if statement so that we can set it to return True or it doesnt do anything
                # and we can return backtrack or else the s = word + s line doesnt run
                if backtrack(s):
                    return True
                # this only runs when it cant find any words, aka it fails
                s = word + s
            # If no word leads to a solution, record failure for this remainder.
            cache[s] = False
            return False

        return backtrack(s)

        # @lc code=end
