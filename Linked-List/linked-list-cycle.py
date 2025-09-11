class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # make sure
        if not head or not head.next:
            return False

        # we use two pinters
        first, last = head.next, head
        
        # do the loop to find if meet each other
        while first != last:
            # if None then no meet
            if not first or not first.next:
                return False
            first = first.next.next
            last = last.next
        return True