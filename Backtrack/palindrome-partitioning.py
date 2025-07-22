class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        def backtrack(i, start):
            if i == n:
                ans.append(path.copy())
                return
            
            # 不分割
            if i < n - 1:
                backtrack(i + 1, start)

            # 分割
            t = s[start: i + 1]
            if t == t[::-1]:
                path.append(t)
                backtrack(i + 1, i + 1)
                path.pop()

        backtrack(0, 0)
        return ans
