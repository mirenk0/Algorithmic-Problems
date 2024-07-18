def find(t):
    dict = {}

    for i, x in enumerate(t):
        if x in dict:
            dict[x].append(i)
            continue

        dict[x] = [i]

    least_lst = []
    for x in dict:
        least_lst.append(max(dict[x]) - min(dict[x]))

    return max(least_lst)



if __name__ == "__main__":
    print(find([1,2,1,1,2])) # 3
    print(find([1,2,3,4])) # 0
    print(find([1,1,1,1,1])) # 4
    print(find([1,1,2,3,4])) # 1
    print(find([1,5,1,5,1])) # 4
