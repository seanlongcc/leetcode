#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0

            # recurse to children
            left = dfs(node.left)
            right = dfs(node.right)

            # get the diameter through this node
            self.max_diameter = max(self.max_diameter, left + right)

            # return the height seen by this node
            return max(left, right) + 1

        dfs(root)
        return self.max_diameter


# @lc code=end
