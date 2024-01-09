def find_leaves(root):
    leaves = []

    def traverse(node):
        if node is None:
            return
        if node.left is None and node.right is None:
            leaves.append(node.value)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return leaves

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    
    def print_tree(self):
        if self.root is None:
            print('Tree is empty')
        else:
            self._print_tree_recursive(self.root, "", True)

    def _print_tree_recursive(self, node, prefix, is_left):
        if node is not None:
            print(prefix + ("└── " if is_left else "├── ") + str(node.value))
            self._print_tree_recursive(node.left, prefix + ("    " if is_left else "│   "), True)
            self._print_tree_recursive(node.right, prefix + ("    " if is_left else "│   "), False)


tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)
tree.print_tree()

print(find_leaves(tree.root))
