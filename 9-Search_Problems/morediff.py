def create(n):
    if n == 2:
        return None
    result = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            result.append(i)
    for i in range(2, n + 1, 2):
        result.append(i)
    return result[:n]


if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # None
    print(create(4)) # [2, 4, 1, 3]
    print(create(7)) # [1, 3, 5, 2, 6, 4, 7]
