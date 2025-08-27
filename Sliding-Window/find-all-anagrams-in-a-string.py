class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        # initialize the length
        len_s, len_p = len(s), len(p)
        # if p is bigger, just return
        if len_p > len_s:
            return []
        # answer list
        answer = []
        # initialize the string list with 26 letters
        s_count = [0] * 26
        p_count = [0] * 26
        # do the loop for the first several letters
        for i in range(len_p):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1
        # if the first equal, add
        if s_count == p_count:
            answer.append(0)

        # do the other loop
        for i in range(len_s - len_p):
            # erease now and append next
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + len_p]) - 97] += 1

            # if equal then append
            if s_count == p_count:
                answer.append(i + 1)

        return answer
        
