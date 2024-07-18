def count(s):
    """How many ways can you choose 2 positions in a bit string, so that each position has same bit"""
    n = len(s)
    zeros = 0
    ones = 0
    total = 0

    for bit in s:
        if bit == '0':
            zeros += 1
        
        if bit == '1':
            ones += 1

    total += zeros * (zeros - 1) // 2 + ones * (ones - 1) // 2
        
    return total

    
def count_brute(bits):
    n = len(bits)
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (bits[i] == '0' and bits[j] == '0') or (bits[i] == '1' and bits[j] == '1'):
                result += 1
    return result


if __name__ == "__main__":
    print(count("0101")) # 2
    print(count("000000")) # 15
    print(count("000111")) # 6
    print(count("00100001101100")) # 46
