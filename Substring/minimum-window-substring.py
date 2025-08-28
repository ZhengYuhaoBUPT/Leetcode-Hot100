class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # we need the t is smaller
        len_s = len(s)
        len_t = len(t)
        if len_t > len_s: return ""
        # initialize the two dicts to record the two
        dict_s, dict_t = defaultdict(int), defaultdict(int)
        # record the t
        for i in t:
            dict_t[i] += 1
        # record the minimum string
        min_string = ""
        # how many char satisfy already
        cnt = 0
        
        # do the loop in s
        # use two pointers left and right
        left, right = 0, 0
        while right < len_s:
            # add the number
            dict_s[s[right]] += 1
            # judge the right place
            if dict_s[s[right]] <= dict_t[s[right]]:
                # means that can not satisfy
                cnt += 1
            # if the number can satisfy on the left
            while left <= right and dict_s[s[left]] > dict_t[s[left]]:
                dict_s[s[left]] -= 1
                left += 1
            # if already satisfy
            if cnt == len(t):
                if not min_string or right - left + 1 < len(min_string):
                    min_string = s[left:right+1]
            right += 1

        return min_string
