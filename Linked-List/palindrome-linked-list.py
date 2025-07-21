class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        vals = []
        current_head = head
        while current_head:
            vals.append(current_head.val)
            current_head = current_head.next
        
        return vals == vals[::-1]
