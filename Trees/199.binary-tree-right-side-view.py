#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs: go level by level and take the visible right value;
        # if there isn't a node further right at that level, the leftmost remaining becomes it.
        if not root:
            return []

        ans = []
        # dfs adds to queue in left to right
        queue = deque([root])

        # Process nodes level by level
        while queue:
            level_size = len(queue)  # Number of nodes in the current level
            # Will hold the visible (rightmost) value for this level
            right_val = None

            # Iterate exactly over the current level's nodes
            for _ in range(level_size):
                node = queue.popleft()   # Take next node in this level
                right_val = node.val     # Overwrite each time; last value after loop = rightmost

                # Enqueue children for the next level.
                # Order matters for our "last processed is rightmost" trick:
                # add left first, then right, so right nodes appear later in the queue.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # After exhausting the level, right_val holds the rightmost node's value
            ans.append(right_val)

# @lc code=end
