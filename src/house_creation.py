import random

class House:
    location_modifiers = [
        {
            "Location": "King’s Landing",
            "Defense": +5,
            "Influence": -5,
            "Lands": -5,
            "Law": +20,
            "Population": +5,
            "Power": -5,
            "Wealth": -5
        },
        {
            "Location": "Dragonstone",
            "Defense": +20,
            "Influence": -5,
            "Lands": -5,
            "Law": +5,
            "Population": 0,
            "Power": 0,
            "Wealth": -5
        },
        {
            "Location": "The North",
            "Defense": +5,
            "Influence": +10,
            "Lands": +20,
            "Law": -10,
            "Population": -5,
            "Power": -5,
            "Wealth": -5
        },
        {
            "Location": "The Iron Islands",
            "Defense": +10,
            "Influence": -5,
            "Lands": -5,
            "Law": 0,
            "Population": 0,
            "Power": +10,
            "Wealth": 0
        },
        {
            "Location": "The Riverlands",
            "Defense": -5,
            "Influence": -5,
            "Lands": +5,
            "Law": 0,
            "Population": +10,
            "Power": 0,
            "Wealth": +5
        },
        {
            "Location": "Mountains of the Moon",
            "Defense": +20,
            "Influence": +10,
            "Lands": -5,
            "Law": -10,
            "Population": -5,
            "Power": 0,
            "Wealth": 0
        },
        {
            "Location": "The Westerlands",
            "Defense": -5,
            "Influence": +10,
            "Lands": -5,
            "Law": -5,
            "Population": -5,
            "Power": 0,
            "Wealth": +20
        },
        {
            "Location": "The Reach",
            "Defense": -5,
            "Influence": +10,
            "Lands": 0,
            "Law": -5,
            "Population": +5,
            "Power": 0,
            "Wealth": +5
        },
        {
            "Location": "The Stormlands",
            "Defense": +5,
            "Influence": 0,
            "Lands": -5,
            "Law": +10,
            "Population": -5,
            "Power": +5,
            "Wealth": 0
        },
        {
            "Location": "Dorne",
            "Defense": 0,
            "Influence": -5,
            "Lands": +10,
            "Law": -5,
            "Population": 0,
            "Power": +10,
            "Wealth": 0
        }
    ]

    def __init__(self):
        self.location = location_for_dice_roll(roll_dice(3))
        self.defense = 1 + random.randint(1, 6)  # Base value of 1
        self.influence = 1 + random.randint(1, 6)  # Base value of 1
        self.lands = 1 + random.randint(1, 6)  # Base value of 1
        self.law = 1 + random.randint(1, 6)  # Base value of 1
        self.population = 1 + random.randint(1, 6)  # Base value of 1
        self.power = 1 + random.randint(1, 6)  # Base value of 1
        self.wealth = 1 + random.randint(1, 6)  # Base value of 1

        # Apply location modifiers
        for location_mod in House.location_modifiers:
            if location_mod["Location"] == self.location:
                self.defense += location_mod["Defense"]
                self.influence += location_mod["Influence"]
                self.lands += location_mod["Lands"]
                self.law += location_mod["Law"]
                self.population += location_mod["Population"]
                self.power += location_mod["Power"]
                self.wealth += location_mod["Wealth"]

    def __str__(self):
        return f"Location: {self.location}\nDefense: {self.defense}\nInfluence: {self.influence}\nLands: {self.lands}\nLaw: {self.law}\nPopulation: {self.population}\nPower: {self.power}\nWealth: {self.wealth}"

def roll_dice(num_dice):
    return sum([random.randint(1, 6) for _ in range(num_dice)])  # Roll num_dice 6-sided dice

def location_for_dice_roll(result):
    if result == 3:
        return "King’s Landing"
    elif result == 4:
        return "Dragonstone"
    elif result in (5, 6):
        return "The North"
    elif result == 7:
        return "The Iron Islands"
    elif result in (8, 9):
        return "The Riverlands"
    elif result in (10, 11):
        return "Mountains of the Moon"
    elif result in (12, 13):
        return "The Westerlands"
    elif result in (14, 15):
        return "The Reach"
    elif result in (16, 17):
        return "The Stormlands"
    elif result == 18:
        return "Dorne"
    else:
        return "Unknown"  # Handle any other result not in the specified range

# Example usage for a House
house = House()

print(str(house))
