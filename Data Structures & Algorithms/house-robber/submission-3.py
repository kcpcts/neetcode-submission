class Solution:
    def rob(self, nums: List[int]) -> int:
        # value(i) = max value i can get from robbing up to and including house i
        # what is this?
        # the max value i can get from robbing up to house i-1, but skipping i's value
        # or the max value i can get from robbing up to house i-2, but then taking i's value
        # max of those two possibilities
        if len(nums) <= 2:
            return max(nums)

        table = [None] * len(nums)
        # table[i] = max value i can get from robbing to house i
        table[0] = nums[0]
        table[1] = max(nums[0],nums[1])

        def value(i):
            if table[i] is not None:
                return table[i]
            else:
                table[i] = max(value(i-1), nums[i] + value(i-2))
            
            return table[i]
        
        return value(len(nums)-1)
