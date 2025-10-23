nums = [7,2,1,5,6,4,8]

# BRUTE FORCE :GENERATE ALL POSSIBLE COMBINATIONS
# def maxProfit(prices):
#     max_profit = 0
#     n = len(prices)
#     for i in range(n):
#         for j in range(i + 1, n):
#             cur_profit = prices[j] - prices[i]
#             max_profit = max(max_profit, cur_profit)
#     return max_profit


# OPTIMAL SOLUTION : KEEP TRACK OF MIN_PRICES
def maxProfit(prices):
    max_profit = 0
    n = len(prices)
    min_price = float("inf")
    for i in range(n):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    return max_profit

print(maxProfit(nums))