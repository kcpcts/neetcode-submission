class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = [None,None,-1]
    # start at some character i
    # left,right = i
    # if left-1 and right+1 are equal: (expand palindrome)
    # left -= 1
    # right += 1
    # update running maximum with s[i:j+1]
    # recurse with new left and right
    # else:
    # return

    # if 
        def check(left,right):
            if left < 0 or right >= len(s):
                return
            if left == right:
                check(left-1,left)
                check(right,right+1)
            
            if s[left] == s[right]:
                if (right-left + 1) > longest[2]:
                    longest[0], longest[1] = left, right 
                    longest[2] = (right-left + 1)
                check(left-1,right+1)
            


        for i,char in enumerate(s):
            check(i,i)
        return s[longest[0]:longest[1]+1]


