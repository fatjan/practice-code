def flatten(root):
    if not root:
        return
    flatten(root.left)
    flatten(root.right)
    if root.left:
        p = root.left
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None