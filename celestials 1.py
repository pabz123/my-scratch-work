import random

# Initial list of cows in each herd
herds = [5, 5, 2]



# Function to implement a winning strategy for bot_move

    # Calculate the XOR sum of all herds

    
    # If no winning move is found, pick randomly (fallback)
    non_zero_herds = [i for i in range(len(cows)) if cows[i] > 0]
    if not non_zero_herds:
        return cows
    herd_to_pick = random.choice(non_zero_herds)
    num_to_pick = random.randint(1, cows[herd_to_pick])
    cows[herd_to_pick] -= num_to_pick
    return cows

# Perform one turn
herds = bot_move(herds)
print(f"bot_move({herds})")