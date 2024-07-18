import random 
import time

def count(t):
    inversionCounter = 0

    while len(t) > 0:
        currMax = max(t)
        currMaxIndex = t.index(currMax)

        for i in range(currMaxIndex, len(t)):
            if currMax > t[i]:
                inversionCounter += 1

        t.remove(currMax)

    return inversionCounter


if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12

    n = 1000
    random.seed(1337)
    nums = [random.randint(1, 10 **6) for _ in range(n)]

    startTime = time.time()
    result = count(nums)
    endTime = time.time()

    print("result:", result)
    print("time:", round(endTime-startTime, 2), "s")
