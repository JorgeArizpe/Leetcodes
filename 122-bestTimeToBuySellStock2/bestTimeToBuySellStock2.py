def maxProfit(prices):
    total = 0
    if len(prices) <= 1:
        return total
    
    buy = prices[0]

    for price in prices:
        if price > buy:
            total += price - buy
        buy = price
    
    return total

prices = [7,1,5,3,6,4]

print(maxProfit(prices))