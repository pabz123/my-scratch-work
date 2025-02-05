

def shafiyu_move(herds):
  """Simulates Shafiyu's move in the cow game.

  Args:
    herds: A list representing the number of cows in each herd.

  Returns:
    A modified list representing the herds after Shafiyu's move.
  """

  # Choose the herd with the most cows
  chosen_herd = herds.index(max(herds))

  # Remove two cows from the chosen herd
  herds[chosen_herd] -= 2

  return herds

# Example usage
initial_herds = [9, 4, 3]
final_herds = shafiyu_move(initial_herds)
print(final_herds)  # Output: [9, 4, 1]


















    