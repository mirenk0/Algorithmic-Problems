def count(x):
    coins = [5, 4, 1]
    count = 0
    for coin in coins:
        count += x // coin
        x %= coin
    return count



if __name__ == "__main__":
    print(count(8)) # 2
    print(count(12345)) # 2469
    print(count(1337**9)) # 2730314408854633746890878156
