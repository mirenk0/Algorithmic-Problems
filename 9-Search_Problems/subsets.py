import itertools

def create(t):
    """
    Create a list of sums of all subsets of the input list `t`.
    """
    # Initialize an empty list to store the subset sums
    subset_sums = [0]  # include the empty subset sum (0)

    for r in range(1, len(t) + 1):
        for subset in itertools.combinations(t, r):
            subset_sum = sum(subset)
            subset_sums.append(subset_sum)

    subset_sums.sort()

    return subset_sums


if __name__ == "__main__":
    print(create([1, 2, 3])) # [0, 1, 2, 3, 3, 4, 5, 6]
    print(create([42, 1337])) # [0, 42, 1337, 1379]
    print(create([1, 1, 1])) # [0, 1, 1, 1, 2, 2, 2, 3]
    print(create([5])) # [0, 5]
