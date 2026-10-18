class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p1 = 0
        p2 = 0
        maxf = 0
        res = 0
        count = [0] * 26

        while p2 < len(s):
            count[ord(s[p2])-ord('A')] += 1 # add to freq map
            maxf = max(count)
            while ((p2-p1 + 1) - maxf) > k:
                count[ord(s[p1])-ord('A')] -= 1
                p1 += 1
            res = max(res,p2-p1+1)


            p2 += 1

        return res
        
