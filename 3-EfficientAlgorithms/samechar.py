def count(s):
    if not s:
        return 0

    total_count = 0
    current_count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1
        else:
            total_count += (current_count * (current_count + 1)) // 2
            current_count = 1

    total_count += (current_count * (current_count + 1)) // 2

    return total_count

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5
