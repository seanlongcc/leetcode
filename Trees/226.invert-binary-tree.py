#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:     # root is None  ➜  no node here
            return       # stop recursing and hand back None (or nothing)

        # swap the pointers *before* you recurse (pre-order swap).
        # since this happens when going down the tree, it swaps all tress under it as well
        root.left, root.right = root.right, root.left

        # 3) Recursively invert the children that you just swapped.
        self.invertTree(root.left)   # formerly root.right
        self.invertTree(root.right)  # formerly root.left

        # this only runs when the recursion of the above 2 recursive calls end
        return root

        # @lc code=end


# Step 0  – depth-0 frame, root = 4
# ─────────────────
#         4
#       /   \
#      2     7
#     / \   / \
#    1   3 6   9


# Step 1  – after swapping 4’s children (still depth-0 frame)
# ───────────────────────
#        [4]
#       /   \
#      7     2
#     / \   / \
#    6   9 1   3
#    ^   ^ ^   ^
#    |   | |   |
# children under 7 and 2
# are **not** swapped yet


# Step 2  – swap at root = 7
# ───────────────────────
#         4
#       /   \
#     [7]     2
#     / \   / \
#    9   6 1   3

# Depth-2 frames for 9 and 6 both hit the base case and return ⟶ back to depth-0.

# New depth-1 frame, root = 2
# Step 3  – swap at root = 2
# ───────────────────────
#         4
#       /   \
#      7    [2]
#     / \   / \
#    9   6 3   1

# Leaves 3 and 1 trigger two quick depth-2 frames (base case).  When they return,
# the call-stack is empty and the tree is fully inverted:
#
#         4
#       /   \
#      7     2
#     / \   / \
#    9   6 3   1
#
# Complexity ‣  O(N) time, O(H) stack space (H = tree height).
