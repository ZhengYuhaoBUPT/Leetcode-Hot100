class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        ss = set(wordDict)
        n = len(s)
        f = [False] * (n + 1)
        f[0] = True

        for i in range(1, n + 1):
            j = i
            while j >= 1 and not f[i]:
                sub = s[j - 1:i]
                if sub in ss:
                    f[i] = f[j - 1]
                j -= 1
        
        return f[n]
