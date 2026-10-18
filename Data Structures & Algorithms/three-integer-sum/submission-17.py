class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        nums = sorted(nums)
        solution = []
        # pick i as candidate. then find j,k between j=i+1 and k=len(nums)-1 such that j+k = -i, i.e. i + j + k = 0
        i = 0
        while i <= len(nums) - 3:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j = i + 1
            k = len(nums)-1
            while j < k: # they cant be equal - cant use same element
                current = nums[j] + nums[k]
                if current == -nums[i]:
                    solution.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                elif current > -nums[i]:
                    k -= 1
                else:
                    j += 1
            i+=1
            

        return solution     

