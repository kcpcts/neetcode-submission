class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        left = 0 # 
        right = 0 #
        current = {}
        
        maximum = -1
        
        while right < len(s):
            if s[right] in current:
                left = max(left, current[s[right]] + 1)
            
            maximum = max(maximum, right-left+1)
            
            current[s[right]] = right
            right+=1
        
        return maximum

        



        
            
