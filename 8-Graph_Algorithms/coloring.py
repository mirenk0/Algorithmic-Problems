

if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1, 2)
    c.add_edge(2, 3)
    c.add_edge(3, 4)
    c.add_edge(1, 4)
    print(c.check()) # True
    c.add_edge(2, 4)
    print(c.check()) # False

