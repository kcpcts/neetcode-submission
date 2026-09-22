class Solution:
    def countSubstrings(self, s: str) -> int:
        sol = 0
        for i in range(len(s)):
            left = i
            right = i
            # odd number length
            while left >= 0 and right < len(s) and s[left] == s[right]:
                sol += 1
                left -= 1
                right += 1
            
            left = i
            right = i+1
            print(f"even number check: {s[left:right+1]}")
            # even number length
            while left >= 0 and right < len(s) and s[left] == s[right]:
                sol += 1
                left -= 1
                right += 1
            
        return sol 
                