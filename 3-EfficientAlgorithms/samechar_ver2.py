def count(s):
    result = 0
    count = 0
    l = len(s)

    for i in range(l):
        if i > 0 and s[i] != s[i-1]:
            count = 0
        count += 1
        result += count

    return result


if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5

