# -- coding: utf-8 --

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i, price in enumerate(prices):
            if i >= len(prices) - 1:
                break
            if prices[i+1] > price:
                max_profit += prices[i+1] - price
                continue
        return max_profit

