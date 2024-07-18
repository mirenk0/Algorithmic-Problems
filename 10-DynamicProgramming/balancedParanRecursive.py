def count_sequences(n, result={}):
    if n == 0:
        return 1
    if n not in result:
        count = 0
        for i in range(2, n + 1, 2):
            count += count_sequences(i - 2) * \
                     count_sequences(n - i)
        result[n] = count
    return result[n]
