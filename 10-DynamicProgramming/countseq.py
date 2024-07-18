def count(t):
    n = len(t)
    dp = [1] * n
    total = 1

    for i in range(1, n):
        for j in range(i):
            if t[i] > t[j]:
                dp[i] += dp[j]
        total += dp[i]

    return total

if __name__ == "__main__":
    print(count([1, 1, 2, 2, 3, 3])) # 26
    print(count([1, 1, 1, 1])) # 4
    print(count([5, 4, 3, 2, 1])) # 5
    print(count([4, 1, 5, 6, 3, 4, 1, 8])) # 37
