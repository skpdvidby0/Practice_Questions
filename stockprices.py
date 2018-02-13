prices=[7, 1, 5, 3, 6, 4]
maxprofit = 0
min1 = float('inf')
for price in prices:
    min1 = min(min1, price)
    profit = price - min1
    maxprofit = max(maxprofit, profit)

print maxprofit
