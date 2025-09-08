# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        # first, we need to get the length
        lengthA = lengthB = 0
        # get the length
        # cache tmpA and tmpB
        tmpA, tmpB = headA, headB
        while tmpA != None:
            tmpA = tmpA.next
            lengthA += 1
        while tmpB != None:
            tmpB = tmpB.next
            lengthB += 1
        # get the gap, because the last numbers are the same
        if lengthB > lengthA:
            lengthA, lengthB = lengthB, lengthA
            headA, headB = headB, headA
        gap = lengthA - lengthB
        # do the loop to get the same length
        while gap != 0:
            headA = headA.next
            gap -= 1
        # do the loop to get the intersect
        while headA != None:
            # if find
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None