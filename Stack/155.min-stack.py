#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        # Initialize two stacks; one to hold the actual stack values,
        self.stack = []
        # and the other to keep track of the minimum value at any given point.
        self.min_stack = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        # keeping track of the min_stack at every new element being added to the stack
        # min of 2 numbers is O(1)
        self.min_stack.append(min(val, self.min_stack[-1]))

        # if val < self.min_stack[-1]:
        #     self.min_stack.append(val)
        # else:
        #     # reappend the min so the stack and min are the same length
        #     self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        # regular pop is O(1)
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
    # @lc code=end


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()
