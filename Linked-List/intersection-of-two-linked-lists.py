class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        lengthA, lengthB = 0, 0
        curA, curB = headA, headB
        while curA != None:
            curA = curA.next
            lengthA += 1

        while curB != None:
            curB = curB.next
            lengthB += 1
        
        curA, curB = headA, headB

        if lengthB > lengthA:
            lengthA, lengthB = lengthB, lengthA
            curA, curB = curB, curA

        gap = lengthA - lengthB
        while gap != 0:
            curA = curA.next
            gap -= 1

        while curA != None:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        
        return None
