class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_prices = prices[0]
        for price in prices:
            min_prices = min(min_prices,price)
            profit = max(profit, price - min_prices)
        return profit

        