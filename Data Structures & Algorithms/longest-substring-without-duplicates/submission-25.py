class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        p1 = 0
        p2 = 0
        window = set()
        ans = -1
        while p2 < len(s):
            if s[p2] in window:
                while s[p2] in window:
                    window.discard(s[p1])
                    p1 += 1
                
                
            window.add(s[p2])
            ans = max(ans,p2-p1+1)

            p2 += 1
        return ans

        # window[p] -> 0
        # window[w] -> 1
        # p1 = 2, p2 is at 2
        # window[w] -> 2
        # window[k] -> 3
        # window[e] -> 4
        # p1 = 5, p2 = 5
        # window[w] -> 5
        # termination