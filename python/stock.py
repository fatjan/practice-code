def maxProfit(prices):
    if len(prices) == 1:
        return 0

    buy = min(prices[: len(prices) - 1])
    print("buy", buy)
    day_buy = prices.index(buy)
    print("day_buy", day_buy)

    sells = prices[day_buy + 1 : len(prices)]
    sell = max(sells)
    print("sell", sell)
    print("sells", sells)

    day_sell = day_buy + sells.index(sell) + 1
    print("day_sell", day_sell)

    profit = sell - buy
    if profit > 0 and day_buy < day_sell:
        return profit

    return 0


print(maxProfit([2, 1, 2, 0, 1]))
