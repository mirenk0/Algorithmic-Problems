def count(a, b, c):
    if (c < a and c < b):
        return 0

    max_a = c // a
    max_b = c // b

    max_overall_1 = max_a
    if (c - (a * max_a) >= b):
        max_overall_1 += 1

    max_overall_2 = max_b
    if (c - (b * max_b) >= a):
        max_overall_2 += 1

    return max(max_overall_1, max_overall_2)


if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4
