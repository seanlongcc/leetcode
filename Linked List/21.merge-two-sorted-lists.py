#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # It usually holds a placeholder value (often 0, None, or a special marker)
        # and is not considered part of the real data.
        # Its only job is to give every algorithm a guaranteed, non-None starting point.
        dummy = tail = ListNode()

        # While both lists still have nodes, always splice the smaller
        # front node onto `tail.next`, then advance the list that was used.
        while list1 and list2:
            # list1’s head is smaller
            if list1.val < list2.val:
                # link it after `tail`
                tail.next = list1
                # advance list1
                list1 = list1.next
            # list2’s head is smaller or equal
            else:
                tail.next = list2
                list2 = list2.next
            # move `tail` to the node we just added
            tail = tail.next

        # Exactly one of the lists is now empty. Attach the *non-empty* remainder
        tail.next = list1 or list2

        # We only ever mutate tail – dummy stays put.
        # Because dummy.next is always pointing at the first real node, by the time we’re finished,
        # returning dummy.next hands back the full merged list.
        return dummy.next

        # @lc code=end
