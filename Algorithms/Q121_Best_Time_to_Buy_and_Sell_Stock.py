# -- coding: utf-8 --

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_value = float('inf')
        max_profit = 0

        for price in prices:
            min_value = min(min_value, price)
            max_profit = max(max_profit, price-min_value)

        return max_profit
