def solve(t, x):
    weights = sorted(t)

    counter = 0
    curr_weight = 0
    for i in weights:
        if i <= x - curr_weight and curr_weight < x:
            curr_weight += i
            counter += 1

    return counter


if __name__ == "__main__":
    print(solve([1, 1, 1, 1], 2)) # 2
    print(solve([2, 5, 3, 2, 8, 7], 10)) # 3
    print(solve([2, 3, 4, 5], 1)) # 0
    print(solve([2, 3, 4, 5], 10**9)) # 4
    print(solve([10**9, 1, 10**9], 10**6)) # 1
