class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 10 1 5 6 7 1
        # calculate profit as if buying on this day, knowing max price to the right.
        # make array representing max price to the right

        suffix = [-1] * len(prices)
        

        mtr = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            suffix[i] = mtr
            if prices[i] > mtr:
                mtr = prices[i]
        print(suffix)
        
        sol = 0
        for p in range(len(prices)):
            sol = max(sol, suffix[p] - prices[p])
        return sol
    
            