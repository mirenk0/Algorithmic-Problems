def find(x, coins):
    result = {}

    result[0] = 0
    for s in range(1, x + 1):
        result[s] = s
        for c in coins:
            if s - c >= 0:
                result[s] = max(result[s], result[s - c] + 1)

    return result[x]

if __name__ == "__main__":
    print(find(5, [1, 2, 5])) # 5
    print(find(10, [1])) # 10
    print(find(8, [1, 2, 3, 4, 5])) # 8
