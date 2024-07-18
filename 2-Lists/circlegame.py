def create(n):
    """ Every second player in the list, n long, leaves and is added to a new list 

        Find proper ordered list of removed players from first list
    """
    if n == 1:
        return [1]

    players = list(range(1, n+1))
    removed = []
    i = 1
    while len(players) > 1:
        removed.append(players.pop(i))
        i = (i + 1) % len(players)

    removed.append(players.pop())

    return removed


if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,5,3,7]
