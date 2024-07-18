def find(t):
    dict = {}

    for x in t:
        if x not in dict:
            dict[x] = 0

        dict[x] += 1

    least = t[0]
    for x in t:
        if dict[x] < dict[least] or (dict[x] == dict[least]):
            least = x

    return least


if __name__ == "__main__":
    print(find([2,1,3,2,3])) # 1
    print(find([5,5,9])) # 9
    print(find([1,2,3,4,1,3,4])) # 2
    print(find([8])) # 8
    print(find([7,1,7,4,4,5,1])) # 5
