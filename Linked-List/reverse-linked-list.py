class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # we can make the next to link to the pre
        cur, pre = head, None
        # first, record the next
        # second, revise the now
        while cur != None:
            # get the next to record
            tmp = cur.next
            # link to the pre
            cur.next = pre
            # revise the pre to the cur
            pre = cur
            # revise the cur to the record
            cur = tmp
        return pre