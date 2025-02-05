def pick_cows(herds):
  """
  Simulates picking cows from three herds until one herd is empty.

  Args:
    herds: A list of three integers representing the number of cows in each herd.

  Returns:
    A list of three integers representing the remaining number of cows in each herd.
  """

  while all(herd > 0 for herd in herds):
    for i in range(3):
      if herds[i] > 0:
        herds[i] -= 1
        break

  return herds

# Example usage:
herds = [10, 15, 20]
remaining_herds = pick_cows(herds)
print(remaining_herds)