#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            # save the spot for the next 'current'
            next_ = current.next
            # the only thing that matters when reversing a list swapping direction of the .next
            # doing this flips the arrow since we are changing the direction of the .next
            current.next = prev
            # now move the prev to the next node
            prev = current
            # move the current to the next node which we saved earlier
            current = next_

        return prev
        # @lc code=end
