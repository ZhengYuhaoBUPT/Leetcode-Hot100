class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        def dfs(i):
            if i == n: # 子集构建完毕
                ans.append(path.copy())
                return

            # 不选
            dfs(i + 1)

            # 选择
            path.append(nums[i])
            dfs(i + 1)
            path.pop() # 恢复现场

        dfs(0)
        
        return ans
