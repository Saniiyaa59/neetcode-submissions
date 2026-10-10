class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        j = 1

        max_profit = 0

        while j < len(prices):
            profit = prices[j] - prices[i]
            max_profit = max(profit, max_profit)
            if prices[i] > prices[j]:
                i = j
            j+=1

        return max_profit