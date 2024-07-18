class RepeatList:
    def __init__(self):
        self.count = {}
        self.status = False

    def add(self, x):
        if x not in self.count:
            self.count[x] = 0
        self.count[x] += 1 

        if self.count[x] > 1:
            self.status = True

    def check(self):
        return self.status

if __name__ == "__main__":
    r = RepeatList()
    print(r.check()) # False
    r.add(1)
    r.add(2)
    r.add(3)
    print(r.check()) # False
    r.add(2)
    print(r.check()) # True
    r.add(5)
    print(r.check()) # True
