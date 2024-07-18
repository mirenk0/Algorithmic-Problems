import time

def test():
    n = 10**5
    numbers = []

    start_time_addition = time.time()
    for s in range(1, n):
        numbers.append(s)
    end_time_addition = time.time()

    start_time_deletion = time.time()
    for _ in numbers:
        numbers.pop()
    end_time_deletion = time.time()

    print("time:", round(end_time_addition - start_time_addition, 3), "s")
    print("time:", round(end_time_deletion - start_time_deletion, 3), "s")


if __name__ == "__main__":
    test()

