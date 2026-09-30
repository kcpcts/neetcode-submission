class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1 2 3 2 2 
        #     
        #     ht  
        #     h t
        #     t h
        #   t h

        # 1 2 3 4 4
        #   t h
        #     t h
        #       t h
        #         th

        t = nums[0]
        h = nums[nums[0]]
        while nums[t] != nums[h]:
            h = nums[h]
            h = nums[h]
            t = nums[t]
        
        t = 0
        while nums[t] != nums[h]:
            t = nums[t]
            h = nums[h]
        return nums[t]




