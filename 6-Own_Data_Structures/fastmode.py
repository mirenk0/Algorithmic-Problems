class FastMode:
    def __init__(self):
        self.count = {}  # Dictionary to store element count
        self.max_count = 0  # Maximum count of any element
        self.mode_candidate = set() # Potential mode element

    def add(self, x, k):
        self.count[x] = self.count.get(x, 0) + k

        if self.count[x] > self.max_count:
            self.max_count = self.count[x]
            self.mode_candidate = {x}
        elif self.count[x] == self.max_count:
            self.mode_candidate.add(x)

    def mode(self):
        return min(self.mode_candidate) if self.mode_candidate else None


if __name__ == "__main__":
    m = FastMode()
    m.add(4, 7)
    print(m.mode()) # 4
    m.add(8, 5)
    print(m.mode()) # 4
    m.add(8, 3)
    print(m.mode()) # 8
    m.add(4, 1)
    print(m.mode()) # 4
