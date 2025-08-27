class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # first we need to create a set for the sub string
        exist = set()
        # second we need to create the right side of the window
        right = 0
        # create the initial length
        length = 0
        # initialze the string s length
        n = len(s)

        # do the loop to find substring length
        for left in range(n):
            # do the right
            while right < n and s[right] not in exist:
                exist.add(s[right])
                right += 1
            
            length = max(length, right - left)
            
            # pop the left
            exist.remove(s[left])
        
        return length
