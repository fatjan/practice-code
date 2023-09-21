class GraphVertex:
    white, gray, black = range(3)
    def __init__(self):
        self.color = GraphVertex.white
        self.edges = []

def is_deadlocked(G):
    """
    >>> G = [GraphVertex() for _ in range(4)]
    >>> G[0].edges.append(G[2])
    >>> G[0].edges.append(G[3])
    >>> G[1].edges.append(G[2])
    >>> G[2].edges.append(G[0])
    >>> G[3].edges.append(G[3])
    >>> is_deadlocked(G)
    True
    >>> G = [GraphVertex() for _ in range(4)]
    >>> G[0].edges.append(G[2])
    >>> G[0].edges.append(G[3])
    >>> G[1].edges.append(G[2])
    >>> G[2].edges.append(G[0])
    >>> is_deadlocked(G)
    True
    >>> G = [GraphVertex() for _ in range(4)]
    >>> G[0].edges.append(G[2])
    >>> G[0].edges.append(G[3])
    >>> G[1].edges.append(G[2])
    >>> is_deadlocked(G)
    False
    """
    all_black = all(vertex.color == GraphVertex.black for vertex in G)
    if all_black:
        return False

    for vertex in G:
        if vertex.color != GraphVertex.black:
            visited = set()
            recursion_stack = set()
            if has_cycle(vertex, visited, recursion_stack):
                return True
    return False

def has_cycle(vertex, visited, recursion_stack):
    if vertex.color == GraphVertex.gray:
        return True

    visited.add(vertex)
    recursion_stack.add(vertex)

    for neighbor in vertex.edges:
        if neighbor not in visited:
            if has_cycle(neighbor, visited, recursion_stack):
                return True
        elif neighbor in recursion_stack:
            return True

    recursion_stack.remove(vertex)
    vertex.color = GraphVertex.gray
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)