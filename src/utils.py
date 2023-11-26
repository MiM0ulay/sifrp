import random


def roll_dice(num_dice):
    return sum([random.randint(1, 6) for _ in range(num_dice)])  # Roll num_dice 6-sided dice


import random


def happen_with_percentage(n, m):
    """
    Simulate an event with a probability of n/m (as a percentage).

    Parameters:
        n (int): The numerator of the probability.
        m (int): The denominator of the probability.

    Returns:
        bool: True if the event happens, False otherwise.
    """
    if not (0 <= n <= m):
        raise ValueError("Both n and m should be non-negative, and n should be less than or equal to m.")

    chance = random.randint(1, m)  # Generate a random number between 1 and m.
    return chance <= n  # Return True if the random number is less than or equal to n, else False.


# Example usage:
n = 30  # Numerator (e.g., 30%)
m = 100  # Denominator (e.g., out of 100)

result = happen_with_percentage(n, m)
print(f"Event happens with a {n}% chance: {result}")
