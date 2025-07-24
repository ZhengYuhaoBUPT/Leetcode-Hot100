# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2, carry = 0):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if l1 is None and l2 is None and carry == 0:
            return None

        s = carry
        if l1:
            s += l1.val
            l1 = l1.next
        if l2:
            s += l2.val
            l2 = l2.next
        
        return ListNode(s % 10, self.addTwoNumbers(l1, l2, s // 10))
