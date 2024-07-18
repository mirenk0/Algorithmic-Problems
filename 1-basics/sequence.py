def generate(n):
    """ Returns the number at the given position
        
        In a list of numbers where each digit is the smallest positive integer that does not 
        occur earlier in the sequence and has same digit in the beginning and end
    """
    seq = [1]
    i = 2
    while len(seq) < n:
        if str(i)[0] == str(i)[-1] and i not in seq:
            seq.append(i)
        i += 1

    return seq[-1]

if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 2
    print(generate(3)) # 3
    print(generate(10)) # 11
    print(generate(123)) # 1141
