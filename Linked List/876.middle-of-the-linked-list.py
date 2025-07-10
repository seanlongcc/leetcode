#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # length = 0
        # current = head
        # mid_node = head

        # while current:
        #     length += 1
        #     current = current.next

        # mid = length // 2

        # while mid > 0:
        #     mid -= 1
        #     mid_node = mid_node.next
        # return mid_node

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

        return slow

        # @lc code=end
