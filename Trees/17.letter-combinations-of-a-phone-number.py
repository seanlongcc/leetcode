#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = []

        letter_dict = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        if len(digits) == 0:
            return []

        def backtracking(i, current):
            # base case
            # because you cant go further than the length of the digits
            if len(current) == len(digits):
                results.append(current)
                return

            # for choice in choices
            # these are the possible paths
            for n in letter_dict[int(digits[i])]:
                # make the choice and add it to the string
                current += n
                # go one option deeper
                backtracking(i+1, current)
                # undo that
                current = current[:-1]

        # pass in these inputs because you built the result from scratch
        backtracking(0, "")
        return results
        # @lc code=end
