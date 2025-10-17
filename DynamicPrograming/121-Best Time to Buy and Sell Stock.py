from typing import List


class Solution:
    # brute force
    def maxProfit_brute(self, prices: List[int]) -> int:     
        maxProft = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                maxProft = max(maxProft, (prices[j] - prices[i]))

        return maxProft
    
    
    def maxProfit(self, prices: List[int]) -> int:     
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
        
        return maxProfit