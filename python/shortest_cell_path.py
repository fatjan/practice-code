# In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc. Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.

# Each location in the path, including the start and the end, must be a 1. Each subsequent location in the path must be 4-directionally adjacent to the previous location.

# It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.

# If the task is impossible, return -1.

# Examples:

# input:
# grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
# sr = 0, sc = 0, tr = 2, tc = 0
# output: 8
# (The lines below represent this grid:)
# 1111
# 0001
# 1111

# grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
# sr = 0, sc = 0, tr = 2, tc = 0
# output: -1
# (The lines below represent this grid:)
# 1111
# 0001
# 1011
# Constraints:

# [time limit] 5000ms
# [input] array.array.integer grid
# 1 ≤ arr.length = arr[i].length ≤ 10
# [input] integer sr
# [input] integer sc
# [input] integer tr
# [input] integer tc
# All sr, sc, tr, tc are valid locations in the grid, grid[sr][sc] = grid[tr][tc] = 1, and (sr, sc) != (tr, tc).
# [output] integer
  
def shortestCellPath(grid, sr, sc, tr, tc):
    
  # breadth first search from source to target
  
    maxr = len(grid)
    maxc = len(grid[0]) if grid[0] else 0
    
    q = []
    q.append((sr, sc, 0))
    
    distance = [
        [
        -1 for i in range(0, maxc)
        ] for i in range(0, maxr)
    ]
    
    # 0 1 2 -1
    # -1 -1 -1 -1
    # -1 -1 -1 -1
    
    # (0,0,0) -> (1,0,1) (0,1,1) (-1,0,1) (0,-1,1)
    # (0,1,1) -> (0,0,2) (-1,1,2) (1,1,2) (0,2,2)
    
    #  0  1  2  3
    # -1 -1 -1  4
    #  8  7  6  5

    # while queue is not empty, we traverse to four different directions up down left right
    while q:
        curr, curc, curd = q.pop(0)
        
        # check the requirements
        if curr < 0 or curc < 0 or curr >= maxr or curc >= maxc:
            continue
        
        if grid[curr][curc] == 0:
            continue
        
        if distance[curr][curc] == -1:
            distance[curr][curc] = curd
            q.append((curr+1, curc, curd+1))
            q.append((curr, curc+1, curd+1))
            q.append((curr-1, curc, curd+1))
            q.append((curr, curc-1, curd+1))
        else:
            distance[curr][curc] = min(curd, distance[curr][curc])

    return distance[tr][tc]

print(shortestCellPath([[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]], 0, 0, 2, 0))