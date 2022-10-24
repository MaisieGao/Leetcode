def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = float("-inf")
    maxProfit = 0
    start = 0
    for end in range(len(prices)):
        if prices[end] > prices[start]:
            profit = prices[end]-prices[start]
        
            maxProfit = max(maxProfit, profit)
        else:
            start = end
    return maxProfit