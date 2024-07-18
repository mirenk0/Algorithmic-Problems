def count(t):
  """
  This function counts the number of sublists in a playlist (represented by integers)
  where no song appears twice in the sublist.

  Args:
      t: A list of integers representing the playlist.

  Returns:
      An integer representing the number of valid sublists.
  """
  res, right, cnt = 0, 0, 0
  seen = set()  # Use a set to store unique songs encountered in the current window

  for left in range(len(t)):
    while right < len(t) and t[right] not in seen:
      # Expand the window to the right until we see a duplicate song
      seen.add(t[right])
      cnt += 1  # Increase the count of unique songs in the window
      right += 1

    # Calculate the number of sublists for the current window size (cnt)
    # We directly add cnt to res for each unique song encountered
    res += cnt

    # Shrink the window from the left by removing the leftmost element
    seen.remove(t[left])
    cnt -= 1

  return res

if __name__ == "__main__":
  print(count([1, 2, 3, 4]))  # 10
  print(count([1, 1, 1, 1]))  # 4
  print(count([5]))          # 1
  print(count([1, 3, 2, 3, 4, 2, 4, 1, 2, 1]))  # 24
