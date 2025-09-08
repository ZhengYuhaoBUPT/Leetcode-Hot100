class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
        # palindrome
        # record as a list
        answer = []
        # do the forward to record
        while head != None:
            answer.append(head.val)
            head = head.next
        return answer == answer[::-1]