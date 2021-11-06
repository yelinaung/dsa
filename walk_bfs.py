from typing import List

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"data: {self.data}, L: {self.left}, R: {self.right}"


def walk_bfs(root: Node):
    if not root:
        return

    queue = [root]
    while queue:
        item = queue.pop(0)
        print(item)

        if isinstance(item.left, Node):
            queue.append(item.left)

        if isinstance(item.right, Node):
            queue.append(item.right)

    return queue

root = Node(2)
root.left = 1
root.right = Node(5)
root.right.left = 8
root.right.right = 9

walk_bfs(root)
