def count(s):
    onesCounter = 0
    zeroCounter = 0

    for i in s:
        if int(i) == 1:
            onesCounter += 1

        if int(i) == 0:
            zeroCounter += 1

    return len(s) - max(onesCounter, zeroCounter)

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4
