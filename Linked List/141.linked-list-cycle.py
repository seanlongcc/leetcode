#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Keep Track of Visited Nodes
        # use a set since we are checking objects, even if the .val might be the same
        # visited_nodes = set()

        # # Use a separate pointer 'current' to walk the list so 'head' always stays pointing at the first node
        # current = head
        # while current:
        #     # check if the node has been visited
        #     if current in visited_nodes:
        #         return True

        #     visited_nodes.add(current)
        #     current = current.next

        # return False

        # Fast and Slow Pointers Method
        fast = head
        slow = head

        # If either fast is None (end of list) or fast.next is None (only one node left)
        # calling fast.next.next would blow up with an AttributeError.
        # by checking that fast.next exists, fast.next.next can still be None and the loop ends on the next run
        # instead of fast.next.next giving an AttributeError with None.next
        # dont need to check 'slow' since if fast is valid, slow is too
        while fast and fast.next:
            # move the pointers first so that we dont get false positives
            # for example on first iter we would be checking head = head
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
        # @lc code=end
