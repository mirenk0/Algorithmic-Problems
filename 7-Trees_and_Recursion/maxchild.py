class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node):
    max_children = 0

    if len(node.children) > max_children:
        max_children = len(node.children)

    for children in node.children:
        max_children = max(max_children, count(children))

    return max_children
        

if __name__ == "__main__":
    tree1 = Node(1, [
                Node(2),
                Node(3, [Node(4, [Node(5), Node(6)])]),
                Node(7, [Node(8), Node(9)])
            ])

    tree2 = Node(1, [Node(2, [Node(3), Node(4)])])

    print(count(tree1)) # 3
    print(count(tree2)) # 2
