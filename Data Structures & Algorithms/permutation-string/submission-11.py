class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1r = [0] * 26
        for char in s1:
            s1r[ord(char)-ord('a')] += 1
        currentr = [0] * 26
        for i in range(len(s1)):
            currentr[ord(s2[i])-ord('a')] += 1 
        if currentr == s1r:
            return True
        l = 0
        r = len(s1) - 1

        while r < len(s2)-1:
            currentr[ord(s2[l])-ord('a')] -= 1
            l += 1
            r += 1
            currentr[ord(s2[r])-ord('a')] += 1
            if currentr == s1r:
                return True
        return False