class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if len(s) < len(t):
            return ""
        
        hs, ht = defaultdict(int), defaultdict(int)
        for char in t:
            ht[char] += 1
        
        res = ""
        left, right = 0, 0
        cnt = 0
        n = len(s)

        while right < n:
            hs[s[right]] += 1
            if hs[s[right]] <= ht[s[right]]:
                cnt += 1
            
            while left <= right and hs[s[left]] > ht[s[left]]:
                hs[s[left]] -= 1
                left += 1

            if cnt == len(t):
                if not res or right - left + 1 < len(res):
                    res = s[left:right+1]

            right += 1

        return res
