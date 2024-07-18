import random
import time

def count_even_1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even_2(numbers):
    return sum(x % 2 == 0 for x in numbers)

if __name__ == "__main__":
    n = 1000
    random.seed(1377)
    numbers = [random.randint(1, 10**7) for _ in range(n)]

    startTime1 = time.time()
    result1 = count_even_1(numbers)
    endTime1 = time.time()

    startTime2 = time.time()
    result2 = count_even_2(numbers)
    endTime2 = time.time()

    print("result 1:", result1)
    print("time:", round(endTime1 - startTime1, 5), "s")

    print("result 2:", result2)
    print("time:", round(endTime2 - startTime2, 5), "s")






