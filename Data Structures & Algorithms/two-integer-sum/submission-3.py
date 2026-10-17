class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return the distinct indices i and j such that they sum to target
        # map of the remaining value -> index
        seen = {}
        for i,n in enumerate(nums):
            if target-n in seen:
                return [seen[target-n],i]
            else:
                seen[n] = i
        return []