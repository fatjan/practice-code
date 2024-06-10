class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.left = TreeNode(6)
node.right.right = TreeNode(7)

def preorder_traversal(node):
    if node is None:
        return
    print(node.val)
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.val)
    inorder_traversal(node.right)

def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.val)

print("Preorder Traversal")
preorder_traversal(node)
print("Inorder Traversal")
inorder_traversal(node)
print("Postorder Traversal")
postorder_traversal(node)