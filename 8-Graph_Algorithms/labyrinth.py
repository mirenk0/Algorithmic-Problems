def count(r):
  """
  This function finds the shortest path from point A to point B in the given labyrinth.

  Args:
      r: A list of strings representing the labyrinth, where '.' is floor and '#' is wall.

  Returns:
      The length of the shortest path from A to B, or -1 if there is no path.
  """
  rows, cols = len(r), len(r[0])
  start_x, start_y = None, None
  end_x, end_y = None, None

  # Find starting and ending positions
  for i in range(rows):
    for j in range(cols):
      if r[i][j] == 'A':
        start_x, start_y = i, j
      if r[i][j] == 'B':
        end_x, end_y = i, j

  if start_x is None or start_y is None or end_x is None or end_y is None:
    return -1  # No starting or ending point found

  # Perform Breadth-First Search (BFS)
  visited = [[False] * cols for _ in range(rows)]
  queue = [(start_x, start_y, 0)]  # (x, y, distance)
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left

  while queue:
    x, y, distance = queue.pop(0)
    if x == end_x and y == end_y:
      return distance  # Found the end point

    if visited[x][y]:
      continue

    visited[x][y] = True

    for dx, dy in directions:
      new_x, new_y = x + dx, y + dy
      if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and r[new_x][new_y] != '#':
        queue.append((new_x, new_y, distance + 1))

  return -1  # No path found

if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7
