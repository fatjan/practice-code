def maxProfit(prices):
    if len(prices) == 1:
        return 0

    buy = min(prices[: len(prices) - 1])
    day_buy = prices.index(buy)

    sells = prices[day_buy + 1 : len(prices)]
    sell = max(sells)

    day_sell = day_buy + sells.index(sell) + 1

    profit = sell - buy
    if profit > 0 and day_buy < day_sell:
        return profit

    return 0


print(maxProfit([2, 1, 2, 0, 1]))
