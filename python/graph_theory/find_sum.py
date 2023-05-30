class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_sum(root):
    if root == None:
        return 0
    return root.data + find_sum(root.left) + find_sum(root.right)

#  Our example tree looks like this:
#         2
#       /   \
#      3     4
#     / \
#    5   6

node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6

print("Sum of all values of this tree is (should print 20):")
print(find_sum(node2))

# Another example:
#         5
#       /   \
#      6     7
#     / \
#    8   9

node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

node5.left = node6
node5.right = node7
node6.left = node8
node6.right = node9

print("Sum of all values of this tree is (should print 35):")
print(find_sum(node5))