class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # hash
        exist = set()
        n = len(s)

        # pointers
        ans, right = 0, 0

        for i in range(n):

            while right < n and s[right] not in exist:
                exist.add(s[right])
                right += 1

            ans = max(ans, right - i)
            exist.remove(s[i])

        return ans
