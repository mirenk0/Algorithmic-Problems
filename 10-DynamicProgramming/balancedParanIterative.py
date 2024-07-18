def count_sequences(n):
    result = [0] * (n + 1)
    result[0] = 1

    for i in range(2, n + 1, 2):
        for j in range(2, i + 1, 2):
            result[i] += result[j - 2] * result[i - j]

    return result[n]
