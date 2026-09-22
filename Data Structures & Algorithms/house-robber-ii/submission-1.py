class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob house 0: cant take house n-1, so 0 to n-2
        # don't rob house 0: cant take house 0, so 1:n-1
        n = len(nums)
        if n <= 2:
            return max(nums)
        

        def rob(houses): # returns solution for houses
            if len(houses) <= 2:
                return max(houses)
            
            table = [None] * len(houses)
            table[0] = houses[0]
            table[1] = max(houses[0],houses[1])

            def value(i): # returns max value for robbing up to house i
                if table[i] is not None:
                    return table[i] # already filled this cell
                else:
                    # value(i) is max of value(i-2) + houses[i]
                    # and value(i-1) <- cant rob houses[i]
                    table[i] = max(value(i-1), value(i-2) + houses[i])
                return table[i]
            
            return value(len(houses)-1)
                
        rob0 = nums[0:n-1] # excludes n-1 onwards: 0 to n-2 inclusive
        skip0 = nums[1:n] # excludes 0 and n: 1 to n-1 inclusive
        return max(rob(rob0),rob(skip0))

