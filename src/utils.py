import random

def roll_dice(num_dice):
    return sum([random.randint(1, 6) for _ in range(num_dice)])  # Roll num_dice 6-sided dice
