def maxProfit(prices):
    if len(prices) == 1:
        return 0

    buy = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > buy:
            profit = max(profit, prices[i] - buy)
        else:
            buy = prices[i]

    return profit


print(maxProfit([3, 2, 6, 5, 0, 3]))
