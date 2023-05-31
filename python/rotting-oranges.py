from collections import deque

def orangesRotting(grid):
    """
    >>> orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    4
    >>> orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
    -1
    """
    time, fresh = 0, 0
    rotten = deque()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                rotten.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
    
    while rotten and fresh:
        time += 1
        for _ in range(len(rotten)):
            x, y = rotten.popleft()
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                    grid[i][j] = 2
                    fresh -= 1
                    rotten.append((i, j))
    
    return time if fresh == 0 else -1

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)