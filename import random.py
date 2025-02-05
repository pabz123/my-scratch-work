import random


def make_move(herds):
    # Select a herd with cows
    available_herds = [i for i, size in enumerate(herds) if size > 0]
    selected_herd = random.choice(available_herds)
    # Pick a random number of cows from the selected herd
    cows_to_pick = random.randint(1, herds[selected_herd])
    herds[selected_herd] -= cows_to_pick
    print(f"Updated Herds: {herds}")
# Initial herd sizes
herds = [1, 2, 1]
make_move(herds)
print("GROUP 7 BCS: THE PIXELS")