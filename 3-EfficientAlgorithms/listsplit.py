def count(t):

    min_element = min(t)
    result = 0
    min_count = 0
    count = t.count(min_element)

    for i in t:
        if i == min_element:
            min_count += 1



if __name__ == "__main__":
    print(count([2,1,1,3])) # 1
    print(count([1,1,1,1])) # 3
    print(count([1,2,3,1,2,3])) # 3
    print(count([1,2,3,4,3,2,1])) # 6
    print(count([4,3,2,1,2,3,4])) # 0
