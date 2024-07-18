def find(t):
    result = 0
    count = 0
    l = len(t)

    if t[-1] != t[0] and t[0] == t[1]:
        return t[-1]

    for n in range(l):
        if t[n] == t[n-1]:
            count += 1
            continue

        result = t[count]

    return result


if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5
