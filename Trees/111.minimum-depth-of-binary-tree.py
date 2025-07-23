#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])

        step = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return step
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            step += 1

# @lc code=end
