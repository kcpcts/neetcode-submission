class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        table = [-1] * len(cost)
        table[0] = cost[0]
        table[1] = cost[1]

        # min cost of taking step i:
        # min( cost of taking step i-2, cost of taking step i-1) + cost of taking step i

        def costdp(i):
            if table[i-1] == -1:
                table[i-1] = costdp(i-1)
            if table[i-2] == -1:
                table[i-2] = costdp(i-2)
            
            table[i] = min(table[i-1],table[i-2]) + cost[i]
            return min(table[i-1],table[i-2]) + cost[i]
        
        costdp(n-1)
        return min(table[n-1],table[n-2])
            
