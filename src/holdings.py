import random
from utils import roll_dice

defense_info = {
    "Superior Castle": {
        "Investment": 50,
        "Time": 144 + roll_dice(10)
    },
    "Castle": {
        "Investment": 40,
        "Time": 96 + roll_dice(10)
    },
    "Small Castle": {
        "Investment": 30,
        "Time": 72 + roll_dice(10)
    },
    "Hall": {
        "Investment": 20,
        "Time": 60 + roll_dice(10)
    },
    "Tower": {
        "Investment": 10,
        "Time": 36 + roll_dice(10)
    }
}

terrain_cost = {
    "Hills": 7,
    "Mountains": 9,
    "Plains": 5,
    "Wetlands": 3
}

location_data = {
    "Dorne": {
        "Terrain": ["Hills", "Mountains", "Plains"],
        "Features": ["Coast", "Community", "Island", "Road", "Ruin", "Water"]
    },
    "Dragonstone": {
        "Terrain": ["Hills", "Plains", "Wetlands"],
        "Features": ["Coast", "Community", "Grassland", "Island", "Road", "Ruin"]
    },
    "Iron Islands": {
        "Terrain": ["Hills", "Plains"],
        "Features": ["Coast", "Community", "Grassland", "Island", "Road", "Ruin"]
    },
    "King's Landing": {
        "Terrain": ["Plains"],
        "Features": ["Coast", "Community", "Grassland", "Road", "Ruin", "Water", "Woods"]
    },
    "Mountains of the Moon": {
        "Terrain": ["Hills", "Mountains"],
        "Features": ["Coast", "Community", "Grassland", "Island", "Road", "Ruin", "Water"]
    },
    "The North": {
        "Terrain": ["Hills", "Mountains", "Plains", "Wetlands"],
        "Features": ["Coast", "Community", "Grassland", "Island", "Road", "Ruin", "Water", "Woods"]
    },
    "The Reach": {
        "Terrain": ["Plains"],
        "Features": ["Coast", "Community", "Grassland", "Island", "Road", "Ruin", "Water"]
    },
    "Riverlands": {
        "Terrain": ["Hills", "Plains", "Wetlands"],
        "Features": ["Community", "Grassland", "Road", "Ruin", "Water"]
    },
    "The Stormlands": {
        "Terrain": ["Hills", "Mountains", "Plains", "Wetlands"],
        "Features": ["Coast", "Community", "Grassland", "Island", "Road", "Ruin", "Water", "Woods"]
    },
    "Westerlands": {
        "Terrain": ["Hills", "Mountains", "Plains"],
        "Features": ["Coast", "Community", "Grassland", "Island", "Road", "Ruin", "Water"]
    }
}

feature_data = {
    "Coast": {"Coast": 3},
    "Grassland": {"Grassland": 1},
    "Island": {"Island": 10},
    "Road": {"Road": 5},
    "Ruin": {"Ruin": 3},
    "Community": {
        "Hamlet": 10,
        "Small Town": 20,
        "Large Town": 30,
        "Small City": 40,
        "Large City": 50
    },
    "Water": {
        "Stream": 1,
        "River": 3,
        "Pond": 5,
        "Lake": 7
    },
    "Woods": {
        "Light": 3,
        "Dense": 5
    }
}


def allocate_defense_holdings(defense_score, defense_info):
    allocated_keys = {}
    for key, value in defense_info.items():
        if value["Investment"] <= defense_score:
            allocated_keys[key] = value["Time"]
            defense_score -=  value["Investment"]
    return allocated_keys


def choose_random_terrain(location, land_score):
    terrains = []
    features = []
    if location in location_data:
        possible_terrain = location_data[location]["Terrain"]
        possible_features = location_data[location]["Features"]
        while(land_score >= 3):
            # Randomly select a terrain based on land score
            terrain_value =  random.choice(possible_terrain)
            if terrain_cost[terrain_value] <= land_score:
                terrains.append(terrain_value)
                land_score -= terrain_cost[terrain_value]
            feature_values =  random.choice(possible_features)
            feature_value = random.choice(list(feature_data[feature_values].keys()))
            if feature_data[feature_values][feature_value] <= land_score: 
                 features.append(feature_value)
                 land_score -=  feature_data[feature_values][feature_value]

    return terrains, features


class house_holdings:
    def __init__(self):
        self.defense_holdings = None
        self.heirs = None
        self.land_holdings = None


defense_score = 22  # Replace with the actual defense score
land_score = 46
location = "Mountains of the Moon"

allocated_keys = allocate_defense_holdings(defense_score, defense_info)
print("Defense Allocated to the House:", allocated_keys)


terrains, features = choose_random_terrain(location, land_score)
print("Terrains Allocated to the House:", terrains)
print("Features Allocated to the House:", features)

