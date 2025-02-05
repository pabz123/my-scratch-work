
import random
from functools import reduce

def xor_sum(herds):
  """Calculates the XOR sum of the herds."""
  return reduce(lambda x, y: x ^ y, herds)

def find_winning_move(herds):
  """Finds a winning move if possible."""
  xor_sum_herds = xor_sum(herds)
  if xor_sum_herds == 0:
    return None  # No winning move exists
  for i, herd in enumerate(herds):
    target = herd ^ xor_sum_herds
    if target <= 0 and target <= herd:
      return i, herd - target  # Herd index and number of cows to take
  return None  # No winning move found

def bot_move(herds):
  """Bot's move: tries to find a winning move, otherwise makes a random move."""
  winning_move = find_winning_move(herds)
  if winning_move:
    return winning_move
  else:
    # Choose a random herd and take a random number of cows
    herd_index = random.randint(0, len(herds) - 1)
    cows_to_take = random.randint(0, herds[herd_index])
    return herd_index, cows_to_take

# Example usage:
herds = [1, 3, 2]  # Initial herd sizes

  
while sum(herds) > 0:
  herd_index, cows_to_take = bot_move(herds)
  herds[herd_index] -=cows_to_take
  print("Pixels:",herds)