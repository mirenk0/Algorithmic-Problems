def solve(n, k):
    # Initialize the list with numbers from 1 to n
    arr = list(range(1, n+1))

    # Perform k steps
    for _ in range(k):
        # Get the first two elements
        first, second = arr[0], arr[1]

        # Move the first two elements to the end of the list in reverse order
        arr = arr[2:] + [second, first]

    # Return the first element of the list after k steps
    return arr[0]


if __name__ == "__main__":
    print(solve(4, 3)) # 4
    print(solve(12, 5)) # 11
    print(solve(99, 555)) # 11
    print(solve(12345, 54321)) # 9875
