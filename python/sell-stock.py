def maxProfit(prices) -> int:
    if len(prices) == 1:
        return 0

    buy = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        print("buy", buy)
        print("prices[i]", prices[i])

        if prices[i] > buy:
            profit += prices[i] - buy
        else:
            buy = prices[i]
        print("profit", profit)

    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
