def count(t):
    numbers = sorted(t)

    max_count = 1
    curr_count = 1

    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i-1] == 1:
            curr_count += 1
        elif numbers[i] - numbers[i-1] == 0:
            curr_count = curr_count
        else:
            curr_count = 1
        max_count = max(curr_count, max_count)

    return max_count


if __name__ == "__main__":
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3
    print(count([15, 14, 9, 7, 10, 8]))
