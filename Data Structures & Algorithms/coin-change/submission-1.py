class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # table[x] = minimum number of coins needed to make amount X
        table = defaultdict(int)

        def dfs(value): # returns minimum # of coins needed to make value
            if table.get(value):
                return table.get(value)
            if value < 0:
                return float('inf')
            if value == 0:
                return 0
            possibilities = [dfs(value-c) for c in coins]
            table[value] = 1 + min(possibilities)
            return table[value]

            
            
        dfs(amount)

        if table[amount] == float('inf'): return -1
        return table[amount]
