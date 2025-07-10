#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Flag that will flip to False the moment we discover
        # any subtree whose left/right heights differ by > 1.
        self.balanced = True

        def dfs(node) -> int:
            """
            Depth-first search that returns the height of `node`’s
            subtree *and* updates `self.balanced` as a side effect.

            Height definition:
              • empty subtree (None) → 0  
              • non-empty subtree   → 1 + max(left height, right height)
            """
            # Base-case: reached past a leaf → height 0
            if not node:
                return 0

            # Recurse down to get the heights of the children
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # If the current node’s subtrees differ in height by > 1,
            # the whole tree cannot be balanced.
            if abs(left_height - right_height) > 1:
                self.balanced = False

            # Return this subtree’s height.
            # +1 accounts for the current node itself, which is one level
            # above its tallest child. Without the +1, every node would
            # report the same height as its tallest child, making the whole
            # tree appear one level shorter than it truly is.
            return max(left_height, right_height) + 1

        # Kick off the recursion from the root.
        dfs(root)

        # The flag now tells us whether *any* imbalance was found.
        return self.balanced

        # @lc code=end
