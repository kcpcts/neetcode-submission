class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        p1 = 0
        p2 = 0
        window = {}
        ans = -1
        while p2 < len(s):
            if s[p2] in window:
                while p1 < len(s) and s[p1] != s[p2]:
                    window.pop(s[p1], None)
                    p1 += 1
                p1 += 1 # skip it
                
            window[s[p2]] = p2
            ans = max(ans,len(window))

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