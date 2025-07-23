#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        # this gives [root] not [[root]], using deque basically gives an existing list more functionality
        queue = deque([root])

        while queue:
            current_level = []
            # having a for loops makes it possible that the queue can become empty, stopping the loop at each level
            # therefore letting us know that the level of the tree has been completed
            for _ in range(len(queue)):
                current_node = queue.popleft()
                current_level.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            result.append(current_level)

        return result

        # @lc code=end
