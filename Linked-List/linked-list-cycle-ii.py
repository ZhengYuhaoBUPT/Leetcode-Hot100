# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # two pointers
        fast = slow = head
        # for the fast
        # 2b - b = kc b = kc
        # b - a = kc - a
        # more a step to the entrance
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # find the meeting
            if fast == slow:
                # find the entrance
                while slow != head:
                    slow = slow.next
                    head = head.next
                return slow
        return None