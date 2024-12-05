#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {'(': ')', '[': ']', '{': '}'}

        for p in s:
            # check if the current iterator is in an open paren, if so add to stack
            if p in parens.keys():
                stack.append(p)
            # check if the current iterator is a closed paren
            elif p in parens.values():
                # check if the stack is empty, if it's empty, that means no open paren, so fail it
                if len(stack) > 0:
                    # pop last open paren in stack, this will always be an open paren
                    open_paren = stack.pop()
                    # compare last open paren, to the current iterator, a closed paren
                    if parens[open_paren] == p:
                        continue
                    else:
                        return False
                else:
                    return False

        # after running above, if stack has left over open parens, return false
        if len(stack) > 0:
            return False

        return True
        # @lc code=end


Solution().isValid(s="([])")
