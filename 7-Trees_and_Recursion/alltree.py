def count(n, k):
    if k > n:
        return 0
    if k == 1:
        return 1
    total = 0
    for i in range(1, n):
        for j in range(k+1):
            total += count(i, j) * count(n-i-1, k-j)
    return total

if __name__ == "__main__":
    print(count(4, 1)) # 1
    print(count(4, 2)) # 3
    print(count(4, 3)) # 1
    print(count(4, 4)) # 0
    print(count(10, 4)) # 1176
