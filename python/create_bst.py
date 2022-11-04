class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_bst(arr):
    if not arr:
        return

    mid = len(arr) // 2

    root = Node(arr[mid])

    root.left = create_bst(arr[:mid])

    root.right = create_bst(arr[mid + 1 :])

    return root


def preorder(node):
    if not node:
        return

    print(node.data)

    preorder(node.left)
    preorder(node.right)


arr = [1, 3, 5, 6, 7, 19, 27]

node = create_bst(arr)

preorder(node)
