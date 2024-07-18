def solve(t):
  """
  Sorts a list using SWAP and MOVE commands.

  Args:
      t: A list of integers.

  Returns:
      A list of strings representing the sequence of commands (SWAP or MOVE).
  """
  commands = []
  n = len(t)
  
  # Iterate through the list
  for i in range(n - 1):
    # Check if the current element is in the correct position
    if t[i] == i + 1:
      continue
    
    # If the first element (1) needs to be moved to its correct position
    if t[i] == 1:
      # Use MOVE commands if the element to swap with is after the current position
      if t[i + 1] > t[i]:
        commands.append("MOVE")
      continue
    
    # Swap the current element with the element at its correct position
    correct_position = t[i] - 1
    while i != correct_position:
      # Use MOVE if the element to swap with is at the end
      if correct_position == n - 1:
        commands.append("MOVE")
        correct_position = t[i] - 1  # Update after the move
      else:
        commands.append("SWAP")
        t[i], t[correct_position] = t[correct_position], t[i]
        correct_position = t[i] - 1
  
  return commands


if __name__ == "__main__":
    print(solve([1, 2])) # e.g. []
    print(solve([2, 1])) # e.g. [SWAP]
    print(solve([1, 3, 2])) # e.g. [SWAP, MOVE]
    print(solve([3, 2, 1])) # e.g. [MOVE, SWAP]
    print(solve([2, 3, 4, 1])) # e.g. [MOVE, MOVE, MOVE]
