from collections import deque
import unittest

def shortestCellPath(grid, sr, sc, tr, tc):
  """
  @param grid: int[][]
  @param sr: int
  @param sc: int
  @param tr: int
  @param tc: int
  @return: int


  Shortest Path = BFS

  Start at the starting path

  Use a Queue

  add the start to the queue

  Loop through all the levels

  if we reach the target, return the distance

  At each level, increment the distance


  RT: O(N*M)

  ST: Queue: O(N*M)   by setting all the visisted nodes to 0 or by using a visited set O(N*M)

  Queue: O(N*M) 

  """

  width = len(grid)
  height = len(grid[0])

  #create the queue
  bfs_queue = deque()
  
  #initialize the queue with tuple
  bfs_queue.append((sr,sc))
  
  #initlaize directions
  directions = ((1,0),(0,1),(-1,0),(0,-1))
  
  #initialize distance
  distance = 0
  
  # loop through all the levels
  while bfs_queue:
    
    #loop throuh one level
    
    queue_size = len(bfs_queue)
    
    for _ in range(queue_size):
      
      #take the current cell
      current_x , current_y = bfs_queue.popleft()
      
      # if we found the target, return the distance
      if current_x == tr and current_y == tc:
        return distance
      
      #visit the next cells
      
      for x_change,y_change in directions:
        
        new_x = current_x + x_change
        new_y = current_y + y_change
        
        if 0 <= new_x < width and 0 <= new_y < height and grid[new_x][new_y] == 1 :
          bfs_queue.append((new_x,new_y))
          grid[new_x][new_y] = 0
    
    #after the level, change the distance
    distance += 1
  
  
  #if task is impossible, return -1
  return -1



class TestShortestCellPath(unittest.TestCase):
  
  def test_1_distance(self):
    
    #arrage
    grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
    sr = 0
    sc = 0
    tr = 0
    tc = 1

    #act
    result = shortestCellPath(grid, sr, sc, tr, tc)
    
    #assert
    self.assertEquals(result,1)
    
  def test_8_distance(self):
    
    #arrage
    grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
    sr = 0
    sc = 0
    tr = 2
    tc = 0

    #act
    result = shortestCellPath(grid, sr, sc, tr, tc)
    
    #assert
    self.assertEquals(result,8)
  
  def test_no_path(self):
    
    #arrage
    grid = [[0, 0, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
    sr = 0
    sc = 0
    tr = 2
    tc = 0

    #act
    result = shortestCellPath(grid, sr, sc, tr, tc)
    
    #assert
    self.assertEquals(result,-1)

#unittest.main(verbosity=2)

  
