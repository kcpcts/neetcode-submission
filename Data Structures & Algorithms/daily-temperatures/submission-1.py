class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # indices
        solution = [0] * len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                solution[i] = stack[-1] - i
            else:
                solution[i] = 0
            stack.append(i)
        
        return solution