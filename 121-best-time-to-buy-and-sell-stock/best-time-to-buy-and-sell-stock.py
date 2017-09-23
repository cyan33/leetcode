# -*- coding:utf-8 -*-


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example 1:
#
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
#
#
#
# Example 2:
#
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.
#


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        
        max_profit = 0
        min_buy = prices[0]
        
        for i in range(len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            
            elif prices[i] - min_buy > max_profit:
                max_profit = prices[i] - min_buy
                
        return max_profit
        
