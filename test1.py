# Given an array with prices across days, give me the best time to buy and sell a product to maximize profit
# Assumptions: 1) You can only buy and sell once
#              2) You cannot sell before you buy
#              3) You cannot buy and sell on the same day

# Example: [1, 2, 3, 4, 5] -> buy on day 1, sell on day 5
#          [5, 4, 3, 2, 1] -> buy on day 1, sell on day 2
#          [1, 2, 3, 2, 1] -> buy on day 1, sell on day 3

# Solution: Iterate through the array and keep track of the minimum price seen so far and the maximum profit seen so far
#           If the current price is less than the minimum price seen so far, update the minimum price
#           If the current price is more than the maximum price seen so far, update the maximum price
#           Return the days to buy and sell

# Time Complexity: O(n)
# Space Complexity: O(1)

def best_time_to_buy_and_sell(prices):
    if len(prices) < 2:
        return None

    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    buy_day = 0
    sell_day = 1

    for i in range(2, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            sell_day = i

    return buy_day, sell_day
