class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # it's a good idea to use deque
        # initialize the length
        n = len(nums)
        # initialize the list
        q = collections.deque()

        # do the loop for k
        for i in range(k):
            # we use q to record the index
            # we make the max on the top
            while q and nums[i] >= nums[q[-1]]:
                # pop the small one
                q.pop()
            # append the number
            q.append(i)

        # use a list to record ans
        ans = [nums[q[0]]]
        # do the loop for other
        for i in range(k,n):
            # we need to pop the biggest if exit the window
            while q[0] <= i - k:
                q.popleft()
            # if bigger, pop the later
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            
            # add the ans
            ans.append(nums[q[0]])

        return ans
