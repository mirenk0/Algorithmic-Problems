class Cities:
    def __init__(self, n):
        self.graph = [[] for _ in range(n)]

    def add_road(self, a, b):
        self.graph[a].append(b)

        if len(self.graph) <= b:
            self.graph.extend([[]] * (b + 1 - len(self.graph)))

        self.graph[b].append(a)

    def has_route(self, a, b):
        visited = set()
        return self.has_route_helper(a, b, visited)

    def has_route_helper(self, a, b, visited):
        visited.add(a)

        if a == b:
            return True

        for neighbor in self.graph[a]:
            if neighbor not in visited:
                if self.has_route_helper(neighbor, b, visited):
                    return True
        
        return False


if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1, 2)
    c.add_road(1, 3)
    c.add_road(4, 5)
    print(c.has_route(1, 5)) # False
    c.add_road(3, 4)
    print(c.has_route(1, 5)) # True
