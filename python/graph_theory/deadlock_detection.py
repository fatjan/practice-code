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
    def has_cycle(cur):
        if cur.color == GraphVertex.gray:
            return True

        cur.color = GraphVertex.gray # marks current vertex as a gray one
        if any(next.color != GraphVertex.black and has_cycle(next)
               for next in cur.edges):
            return True
        cur.color = GraphVertex.black # marks current vertex as black one
        return False

    return any(vertex.color == GraphVertex.white and has_cycle(vertex)
               for vertex in G)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


# G = [GraphVertex() for _ in range(4)]
# G[0].edges.append(G[2])
# G[0].edges.append(G[3])
# G[1].edges.append(G[2])
# G[2].edges.append(G[0])
# G[3].edges.append(G[3])

# for vertex in G:
#     print("Vertex Color:", vertex.color)
#     for edge in vertex.edges:
#         print("Edge Color:", edge.color)