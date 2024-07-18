class MaxList:
    def __init__(self):
        self.list = []
        self.status = 0

    def add(self, x):
        self.list.append(x)

        self.status = max(self.status, x)

    def max(self):
        if len(self.list) == 0:
            return None

        return self.status 


if __name__ == "__main__":
    m = MaxList()
    print(m.max()) # None
    m.add(1)
    m.add(2)
    m.add(3)
    print(m.max()) # 3
    m.add(8)
    m.add(5)
    print(m.max()) # 8
