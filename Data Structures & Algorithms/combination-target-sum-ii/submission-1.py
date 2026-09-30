class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        
        # at each step:
        # pick element + skip all of same, combination sum on the rest of the array
        path = []
        solution = []
        def dfs(index, total):
            if total == target:
                solution.append(path.copy())
                return
            if index >= len(nums) or total > target:
                return
            # do the pick vs dont pick
            path.append(nums[index])
            dfs(index + 1, total+nums[index])

            #backtrack
            path.pop()
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            dfs(index + 1, total)

        
        dfs(0,0)
        return solution


            