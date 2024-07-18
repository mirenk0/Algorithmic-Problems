import itertools

def count(n, k, x):
    if k < 0 or x < k or x > n*k or n > 10 or k > n:
        return 0
    if k == 1:
        return 1 if x <= n else 0
    res = 0
    nums = [i for i in range(1, n+1)]
    for subset in itertools.combinations(nums, k):
        if sum(subset) == x:
            res += 1
    return res


if __name__ == "__main__":
    print(count(1, 1, 1)) # 1
    print(count(5, 2, 6)) # 2
    print(count(8, 3, 12)) # 6
    print(count(10, 4, 20)) # 16
