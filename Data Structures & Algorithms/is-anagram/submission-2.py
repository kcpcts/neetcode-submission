class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # frequency maps equal? -> return True, else False
        return Counter(s) == Counter(t)