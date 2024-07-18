def count(x, coins):
    dp = [0] * (x + 1)
    ways = [0] * (x + 1)
    dp[0] = 0
    ways[0] = 1

    for i in range(1, x + 1):
        dp[i] = x + 1
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                ways[i] = ways[i - coin]
            elif i >= coin and dp[i - coin] + 1 == dp[i]:
                ways[i] += ways[i - coin]

    return ways[x]


if __name__ == "__main__":
    print(count(5, [1])) # 1
    print(count(5, [1, 2, 3, 4])) # 4
    print(count(13, [1, 2, 5])) # 12
    print(count(42, [1, 5, 6, 17])) # 30
