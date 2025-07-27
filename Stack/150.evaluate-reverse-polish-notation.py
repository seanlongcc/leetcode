#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token in operators:
                last = stack.pop()
                second_last = stack.pop()
                if token == '+':
                    stack.append(second_last + last)
                elif token == '-':
                    stack.append(second_last - last)
                elif token == '*':
                    stack.append(second_last * last)
                else:
                    stack.append(int(second_last / last))
            else:
                stack.append(int(token))
        return stack.pop()


# @lc code=end
