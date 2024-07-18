def find(t):
    if not t:
        return []

    dp = [[num] for num in t]

    for i in range(1, len(t)):
        for j in range(i):
            if t[i] > t[j] and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [t[i]]

    return max(dp, key=len)


if __name__ == "__main__":
    print(find([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find([1, 1, 1, 1])) # [1]
    print(find([5, 4, 3, 2, 1])) # [3]
    print(find([4, 1, 5, 6, 3, 4, 1, 8])) # [1, 3, 4, 8]
