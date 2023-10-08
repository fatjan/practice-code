# class Node:
#     def __init__(self, val=0):
#         self.left = None
#         self.right = None
#         self.value = val

# def preorder(node):
#     if node is not None:
#         print(node.value)
#         preorder(node.left)
#         preorder(node.right)

# def inorder(node):
#     if node is not None:
#         indorder(node.left)
#         print(node.value)
#         inorder(node.right)

# def postorder(node):
#     if node is not None:
#         postorder(node.left)
#         postorder(node.right)
#         print(node.value)

def TreeConstructor(strArr):
    """
    >>> TreeConstructor(["(1,2)", "(2,4)", "(7,2)"])
    True
    >>> TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"])
    False
    >>> TreeConstructor(["(2,5)", "(2,6)"])
    False
    >>> TreeConstructor(["(10,20)", "(20,50)", "(20,60)", "(50,100)"])
    False
    >>> TreeConstructor(["(10,20)"])
    True
    >>> TreeConstructor(["(2,3)", "(1,2)", "(4,9)", "(9,3)", "(12,9)", "(6,4)"])
    True
    >>> TreeConstructor(["(5,6)", "(6,3)", "(2,3)", "(12,5)"])
    True
    >>> TreeConstructor(["(10,20)", "(20,50)"])
    True
    """
    parents = {}
    children = {}

    for item in strArr:
        parts = item.strip('()').split(',')
        child = int(parts[0])
        parent = int(parts[1])
        if parent in parents:
            parents[parent].append(child)
            if len(parents[parent]) > 2:
                return False
        else:
            parents[parent] = [child]
        
        if child in children:
            return False
        else:
            children[child] = parent

    return True

# TreeConstructor(["(10,20)", "(20,50)", "(20,60)", "(50,100)"])
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)