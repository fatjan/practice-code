# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        def preorder_print(node):
            if node is not None:
                print(node.val)
                preorder_print(node.left)
                preorder_print(node.right)
        preorder_print(root)
        def preorder(node):
            if node is not None:
                print('node', node.val)
                if node.left:
                    print('node left', node.left.val)
                    req1 = node.left.val < node.val
                    if not req1:
                        return False
                if node.right:
                    print('node right', node.right.val)
                    req2 = node.right.val > node.val
                    if not req2:
                        return False
                preorder(node.left)
                preorder(node.right)
        
        preorder(root)
        return True

Solution().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3)))
Solution().isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))))