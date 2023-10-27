def is_valid_bst(root) -> bool:
    def valid(node, left, right):
        if not node:
            return True
        
        if not (node.val < right and node.val > left):
            return False
        
        return valid(node.left, left, node.val) and valid(node.right, node.val, right)
    
    return valid(root, float("-inf"), float("inf"))

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

node = TreeNode(5)
node.left = TreeNode(1)
node.right = TreeNode(4)
node.right.left = TreeNode(3)
node.right.right = TreeNode(6)
print(is_valid_bst(node)) # False

node = TreeNode(2)
node.left = TreeNode(1)
node.right = TreeNode(3)
print(is_valid_bst(node)) # True