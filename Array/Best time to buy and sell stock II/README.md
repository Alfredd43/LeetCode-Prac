# Best Time to Buy and Sell Stock II

## Problem (in simple words)
You are given a list of stock prices for each day. You can buy and sell the stock as many times as you want (but you must sell before you buy again). Find the maximum profit you can make.

## Example
Suppose you have:
- `prices = [7, 1, 5, 3, 6, 4]`

You can:
- Buy at 1, sell at 5 (profit = 4)
- Buy at 3, sell at 6 (profit = 3)
- Total profit = 4 + 3 = 7

## How to Solve (Step by Step)
1. Go through the list of prices.
2. Every time the price goes up from one day to the next, add the difference to your profit.
3. Keep doing this for all days.

## Beginner-Friendly Python Solution
```python
class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit
```

## Constraints
- You can buy and sell as many times as you want.
- You must sell before you buy again.
- The list of prices will have at least 1 price. 