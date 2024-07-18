def count(a, b):
    b_indices = [0] * len(b)
    for i, x in enumerate(b):
        b_indices[x - 1] = i
    count = 0
    for i, x in enumerate(a):
        if b_indices[x - 1] > i:
            count += 1
    return count
   
if __name__ == "__main__":
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([1,2,3,4], [1,2,3,4])) # 0
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5
