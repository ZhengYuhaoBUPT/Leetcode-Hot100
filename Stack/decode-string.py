class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # imitate the recursion
        stack = [] # stack
        res = '' # tmp for the result
        k = 0 # digit for the number

        # loop for the string
        for c in s:
            # if the c is alpha
            if c.isalpha():
                res += c
            # if the c is digit
            elif c.isdigit():
                k = k * 10 + int(c)
            # if the c is the left bracket
            elif c == '[':
                # use the stack, put k numbers of the after
                stack.append((res, k))
                res = ''
                k = 0
            # remaining, c is the right bracket
            else:
                pre_res, pre_k = stack.pop()
                res = pre_res + pre_k * res
        
        return res
