class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_target_level(root, target, lvl=0):
    if root is None:
        return 
    if root == target:
        global target_lvl 
        target_lvl = lvl
        return 
    find_target_level(root.left, target, lvl+1)
    find_target_level(root.right, target, lvl+1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
target = root.left.left

find_target_level(root, target)

print(target_lvl)