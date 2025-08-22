class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        # final result
        res = 0

        # add the last height as 0 to make every element can calculate
        heights.append(0)

        # using stack
        stack = []

        # do the loop in the list, and every num in the list
        # we will search whether the right is smaller
        # if smaller: revise the height and calculate the res to compare
        # if bigger: just append and do nothing
        n = len(heights)
        for i in range(n):
            # if now is smaller, append and revise height
            while stack and heights[stack[-1]] > heights[i]:
                # get the height using pop, because the left and right
                # of this number both smaller
                h = heights[stack.pop()]

                # After getting the height, we calculate the width
                # if the first right height is popped, then if the 
                # second right height also need pop, the width will add
                w = i - stack[-1] - 1 if stack else i
                
                # compare the res
                res = max(res, h * w)
            
            stack.append(i)
        return res

                
