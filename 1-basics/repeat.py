def find(s):
    """Find length of the shortest repeating substring in the given string"""
    n = len(s)
    for pre in range(1, n // 2 + 1):
        if s[:pre] * (n // pre) == s:
            return pre
    return n


if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7
