import collections

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

def search_maze(maze, s, e):
    """
    >>> search_maze([[0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0]], Coordinate(3, 0), Coordinate(0, 0))
    [Coordinate(x=3, y=0), Coordinate(x=2, y=0), Coordinate(x=1, y=0), Coordinate(x=1, y=1), Coordinate(x=1, y=2), Coordinate(x=0, y=2), Coordinate(x=0, y=1), Coordinate(x=0, y=0)]
    >>> search_maze([[0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0]], Coordinate(3, 0), Coordinate(0, 3))
    []
    >>> search_maze([[0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0]], Coordinate(3, 0), Coordinate(0, 1))
    [Coordinate(x=3, y=0), Coordinate(x=2, y=0), Coordinate(x=1, y=0), Coordinate(x=1, y=1), Coordinate(x=0, y=1)]
    >>> search_maze([[0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0]], Coordinate(3, 0), Coordinate(0, 2))
    [Coordinate(x=3, y=0), Coordinate(x=2, y=0), Coordinate(x=1, y=0), Coordinate(x=1, y=1), Coordinate(x=1, y=2), Coordinate(x=0, y=2)]
    >>> search_maze([[0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0]], Coordinate(3, 0), Coordinate(0, 3))
    []
    """
    # Perform DFS to find a feasible path.
    def search_maze_helper(cur):
        # Checks cur is within maze and is a white pixel.
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x]) and maze[cur.x][cur.y] == WHITE):
            return False
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == e:
            return True
        
        if any(map(search_maze_helper, (Coordinate(cur.x - 1, cur.y), Coordinate(cur.x + 1, cur.y), Coordinate(cur.x, cur.y - 1), Coordinate(cur.x, cur.y + 1)))):
            return True
        
        # Cannot find a path, remove the entry added in path.append(cur).
        del path[-1]
        return False
    
    path = []
    if not search_maze_helper(s):
        return [] # No path between s and e.
    return path

import doctest
doctest.testmod(verbose=True)