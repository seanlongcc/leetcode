#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # An empty tree is a valid BST
        if not root:
            return True

        # For the root node, we set:
        #   low  = -infinity  (no lower bound)
        #   high = +infinity  (no upper bound)
        # These bounds will be checked against root.val on the first iteration.
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, low, high = queue.popleft()
            val = node.val

            # Check the current node's value against its allowed range:
            #   low < val < high
            # On the very first pass, this enforces:  -∞ < root.val < +∞
            if val <= low or val >= high:
                return False

            # Left subtree: all values must be < node.val
            if node.left:
                # tighten the upper bound since the left node cant be higher than the parent
                # inherit the same low bound, but update high to node.val
                queue.append((node.left, low, val))

            # Right subtree: all values must be > node.val
            if node.right:
                # tighten the lower bound since the right node cant be lower than the parent
                # update low to node.val, inherit the same high bound
                queue.append((node.right, val, high))

        return True
    # @lc code=end
