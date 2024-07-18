def count(s):
  """
  Counts the number of unique squares visited by the robot.

  Args:
      s: The robot's move sequence string.

  Returns:
      The number of unique squares visited by the robot.
  """

  x, y = 0, 0
  visited = {(0, 0)}
  for char in s:
      if char == 'U':
          y += 1
      elif char == 'D':
          y -= 1
      elif char == 'L':
          x -= 1
      elif char == 'R':
          x += 1
      visited.add((x, y))
  return len(visited)

if __name__ == "__main__":
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2
