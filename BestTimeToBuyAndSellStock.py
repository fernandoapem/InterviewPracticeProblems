from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = max_current_profit = 0
        min_value = prices[0]
        for x in range(1,len(prices)):
            max_current_profit = prices[x] - min_value
            if max_current_profit > profit:
                profit = max_current_profit
            if prices[x] < min_value:
                min_value = prices[x]
        return profit
    def maxProfit2(self, prices: List[int]) -> int: #two pointer
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r]-prices[l])
            else:
                l = r
            r += 1
        return maxProfit



p = Solution()
test = [7,1,5,3,6,4]
test2 = [7,6,4,3,1]
print(p.maxProfit2(test))
print(p.maxProfit(test2))

#price -> 0
#max -> 0
#prices[price] -> [0]7
#prices[future_price] -> [0]7 , [1]1 , [2]5