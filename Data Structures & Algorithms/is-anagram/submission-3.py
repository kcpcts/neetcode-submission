class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # frequency maps equal? -> return True, else False
        sr = [0] * 26
        tr = [0] * 26
        for char in s:
            sr[ord(char)-ord('a')] += 1
        for char in t:
            tr[ord(char)-ord('a')] += 1
        return sr == tr