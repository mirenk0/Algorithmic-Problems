class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def get_subtree_size(node):
    if not node:
        return 0

    size = 1
    for child in node.children:
        size += get_subtree_size(child)

    return size

def count(node):
    if not node:
        return 0

    child_sizes = [get_subtree_size(child) for child in node.children]

    if all(size == child_sizes[0] for size in child_sizes[1:]):
        return 1 + sum(count(child) for child in node.children)
    else:
        return sum(count(child) for child in node.children)


if __name__ == "__main__":
    tree = Node(1, [
               Node(2),
               Node(3, [Node(4, [Node(5), Node(6)])]),
               Node(7, [Node(8), Node(9)])
           ])

    print(count(tree)) # 8
