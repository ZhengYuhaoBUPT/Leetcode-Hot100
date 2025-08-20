class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        n = len(temperatures)

        # get the result list
        ans = [0] * n
        # use the stack to find and sort the temperatures
        stack = []
        
        # do the loop
        for i in range(n):
            # temperature now time
            temperature = temperatures[i]

            # loop in the stack
            # if the temperature is bigger than the lowest temperature
            # in the stack, then we need to pop the lowest
            while stack and temperature > temperatures[stack[-1]]:
                pop_index = stack.pop()
                # and record the ans
                ans[pop_index] = i - pop_index
            
            # append the temperature now time
            stack.append(i)

        return ans
