"""
Problem:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]


Understanding:
- Breadth First Search - any nodes connecting to the source that is the same & can create a 4-directional combination will also be affected 
- The color of the nearby cells need to be the same as the source cell in order to change them

- Working cases are set in the CodePath page 
- Additional Case: source node is different from all other nodes 
- Non working case - Out of Range or Negative Range

- Edge Case: Empty Set
      0     1     2
0  (0,0) (0,1) (0,2)        
1  (1,0) (1,1) (1,2)
2  (2,0) (2,1) (2,2)

Matching:
- BFS
- Queue (FIFO)

Planning:
1) Get the color for the starting node (coordinate is in input)
2) Implement BFS by 
  - while loop 
  - check if there are neighboring nodes that are similar       to starting node (color)
  - if that's the case > push them to queue
  - if not, don't add it 
  - push coordinate > use coordinate to change color (FIFO)
  

Implement:


Review:


Evaluate:

"""

def FloodFill(image, sr, sc, newColor):
  new_image = image
  max_row = len(image)
  max_col = len(image[0])
  initial_color = image[sr][sc]
  new_image[sr][sc] = newColor
  queue = []
  queue.append([sr,sc])
  
  while(len(queue) != 0):
    cell = queue.pop(0)
    row = cell[0]
    col = cell[-1]
    if (row - 1) != -1 and new_image[row-1][col] == initial_color: 
      new_image[row-1][col] = newColor
      queue.append([(row-1),col])
    if (col - 1) != -1 and new_image[row][col-1] == initial_color:
      new_image[row][col-1] = newColor
      queue.append([row,(col-1)])
    if (row + 1) != max_row and new_image[row+1][col] == initial_color:
      new_image[row+1][col] = newColor
      queue.append([(row+1),col])
    if (col + 1) != max_col and new_image[row][col+1] == initial_color:
      new_image[row][col+1] = newColor
      queue.append([row,(col+1)])

  return new_image


print(FloodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
print(FloodFill([[0,0,0],[0,0,0]], 0, 0, 2))
    
