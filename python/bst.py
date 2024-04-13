class Node:
    def __init__(self, value=0) -> None:
        self.value = value
        self.left = None
        self.right = None

def create_binary_search_tree(node_values):
    root = Node(node_values[0])
    for i in range(1, len(node_values)):
        current = root
        node = Node(node_values[i])
        while current:
            if node.value <= current.value:
                if not current.left:
                    current.left = node
                    break
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = node
                    break
                else:
                    current = current.right
    return root

def print_pre_order(node):
    if node is None:
        return
    
    print(node.value, end = " ")
 
    print_pre_order(node.left)
 
    print_pre_order(node.right)

tree = create_binary_search_tree([5, 3, 7, 2, 4, 6, 8])
print_pre_order(tree)

def is_node_exist(root, value):
    current = root
    while current:
        if value == current.value:
            return True
        elif value <= current.value:
            if current.left:
                current = current.left
            else:
                current = current.right
        else:
            if current.right:
                current = current.right
            else:
                current = current.left
    return False

print()
print(is_node_exist(tree, 3))
print(is_node_exist(tree, 9))

# Output:
# 5 3 2 4 7 6 8 
# True
# False
    