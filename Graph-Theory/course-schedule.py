class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # we need to find if there is a loop
        # a stack for every list
        g = [[] for _ in range(numCourses)]
        # for every class, we get its prerequisites
        for a, b in prerequisites:
            g[a].append(b)

        # we need to record whether the number is under process
        colors = [0] * numCourses

        # we need to write a loop to do dfs
        def dfs(x):
            # first record the now class as 1 (under process)
            colors[x] = 1

            # check every prerequsite before x
            for y in g[x]:
                # if y is under process
                # or y is not found before, and 
                if colors[y] == 1 or (colors[y] == 0 and dfs(y)):
                    # we find loop
                    return True
            # we do not find the loop
            colors[x] = 2
            return False
                
        # do the loop for every number
        for now_class, pre_class in enumerate(colors):
            # if the number is not under process
            # and the dfs(number) find the loop
            if pre_class == 0 and dfs(now_class):
                return False
        
        return True
