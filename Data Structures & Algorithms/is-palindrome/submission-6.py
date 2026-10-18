class Solution:
    def isPalindrome(self, s: str) -> bool:
        # p1 and p2 at the start and end of s
        # invariant must hold. string length is even or odd:
        # pointers are equal until they cross each other
        # p1 advances forward
        # p2 advances backward

        # clean the string of extraneous punctuation
        s = "".join(char.lower() for char in s if char.isalnum())
        print(s)


        p1 = 0
        p2 = len(s)-1
        while p1 <= p2: # need the = case for odd length strings
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        # if we reach this line we know the invariant held.
        # so we can return true.
        return True