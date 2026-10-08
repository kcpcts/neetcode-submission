class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        tps = sorted(zip(position,speed))

        times = [(target-p)/s for p,s in tps]
        for i in range(len(times)-1, -1, -1):
            
            if stack:
                if stack[-1] < times[i]:
                    stack.append(times[i])
            else:
                stack.append(times[i])
        
        return len(stack)
                

