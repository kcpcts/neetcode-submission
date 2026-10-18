class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # either we pick the current element or we don't pick it.
        solution = []
        path = []
        def dfs(i):
            if i == len(nums):
                solution.append(path.copy())
                return
            
            # pick the current element and continue
            path.append(nums[i])
            
            dfs(i+1)
            

            # dont pick the current element and continue
            path.pop()
            dfs(i+1)

        dfs(0)

        return solution
