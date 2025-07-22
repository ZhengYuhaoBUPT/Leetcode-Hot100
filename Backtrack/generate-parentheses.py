class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = [''] * (n * 2)

        def backtrack(left, right):
            if right == n:
                ans.append(''.join(path))
                return
            
            if left < n:
                path[left + right] = '('
                backtrack(left + 1, right)

            if right < left:
                path[left + right] = ')'
                backtrack(left, right + 1)
                
        backtrack(0, 0)
        return ans
