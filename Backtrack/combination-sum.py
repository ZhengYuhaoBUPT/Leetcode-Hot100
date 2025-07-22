class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(i, left):
            if left == 0:
                ans.append(path.copy())
                return
            
            if i == len(candidates) or left < 0:
                return

            # 不选
            backtrack(i + 1, left)

            # 选择
            path.append(candidates[i])
            backtrack(i, left - candidates[i])
            path.pop()

        backtrack(0, target)
        return ans
