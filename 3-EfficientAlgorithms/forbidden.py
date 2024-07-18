def count(s):
    l = len(s)
    result = 0
    count = 0

    for e in range(l):
        if e >= 0 and s[e] == 'a':
            count = 0
            continue

        count += 1
        result += count

    return result

if __name__ == "__main__":
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1
    print(count("aybabtu")) # 9
