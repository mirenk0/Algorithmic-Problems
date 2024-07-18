class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node):
    return sum(count_helper(node, 0))

def count_helper(node, depth=0):
    depths = [depth]

    for children in node.children:
        depths += count_helper(children, depth + 1)

    return depths

if __name__ == "__main__":
    tree = Node(1, [
               Node(2),
               Node(3, [Node(4, [Node(5), Node(6)])]),
               Node(7, [Node(8), Node(9)])
           ])

    print(count(tree)) # 15
