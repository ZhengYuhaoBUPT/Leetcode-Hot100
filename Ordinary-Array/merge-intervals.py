class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # first sort the intervals by the first index
        # of every list []
        intervals.sort(key=lambda x:x[0])
        # initialize ans
        ans = []

        # do the loop in the intervals
        for interval in intervals:
            # if there's no ans and not have the same lap
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            # else we need to overlap the interval
            else:
                # the last number in ans
                # have the largest number between the numbers
                ans[-1][1] = max(ans[-1][1],interval[1])
        return ans
