def maxProfit(prices):
    if not bool(prices):
        return

    minimum = prices[0]
    maxWins = 0

    for price in prices:
        if price > minimum and price - minimum > maxWins:
            maxWins = price - minimum
        elif price < minimum:
            minimum = price

    return maxWins


prices = [7, 1, 5, 3, 6, 4]

print(maxProfit(prices))
