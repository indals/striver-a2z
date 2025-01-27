class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        max_profit = 0
        lowet_price = prices[0]

        for index in range(1, len(prices)):
            max_profit = max(max_profit, prices[index]-lowet_price)
            lowet_price = min(prices[index], lowet_price)
        return max_profit

            