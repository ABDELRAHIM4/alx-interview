#!/usr/bin/python3


"""determine the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet total"""
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    if total <= 0:
        return 0
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return (dp[total] if dp[total] != float('inf') else -1)
