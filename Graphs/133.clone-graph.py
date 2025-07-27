#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # ─────────────────────────────────────────────────────────────────────
        # If the input graph is empty, there is nothing to clone.
        # ─────────────────────────────────────────────────────────────────────
        if not node:
            return None

        # ─────────────────────────────────────────────────────────────────────
        # Breadth‑First Search (BFS) setup
        #   • `queue`  – queue of **original** nodes to visit
        #   • `map` – dictionary that maps each original node → its cloned copy
        # ─────────────────────────────────────────────────────────────────────
        queue = collections.deque([node])

        # ⚠️  We *call* the class:  Node(node.val)
        #     ─────────────────────────────────────
        #     This runs Node.__init__(...), giving us a *brand‑new* object whose
        #     value matches the original.  It starts with an empty neighbors list
        #     because we haven’t wired up any edges yet.
        #
        #     Contrast:
        #       • Reading an existing attribute → root.left, root.val, etc.
        #         (Just peeking inside an already‑built object.)
        #       • Calling the class            → Node(x)
        #         (Constructing a fresh object that’s independent of the original.)
        # ─────────────────────────────────────────────────────────────────────
        map = {node: Node(node.val)}

        # ─────────────────────────────────────────────────────────────────────
        # Standard BFS loop
        # ─────────────────────────────────────────────────────────────────────
        while queue:
            # current node being processed
            current = queue.popleft()

            # Examine each neighbor (edge u‑v)
            for neighbor in current.neighbors:
                # Have we cloned this neighbor yet?
                if neighbor not in map:
                    # No → build its *own* copy
                    map[neighbor] = Node(neighbor.val)
                    # and queue the neighbor for BFS
                    queue.append(neighbor)

                # Wire up the edge in the *cloned* graph:
                # append(copy_of_v) to neighbors of copy_of_u
                map[current].neighbors.append(map[neighbor])

        # The clone corresponding to the start node is the entry point to the
        # fully cloned (deep‑copied) graph.
        return map[node]
# @lc code=end
