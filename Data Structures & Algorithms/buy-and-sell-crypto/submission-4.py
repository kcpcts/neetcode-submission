class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for each day, profit is day - min price to left
        minprice = float('inf')
        sol = 0
        for p in prices:
            minprice = min(minprice,p)
            profit = p - minprice
            sol = max(sol,profit)
        return sol