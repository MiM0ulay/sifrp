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
        self.defense = roll_dice(7)
        self.influence = roll_dice(7)
        self.lands = roll_dice(7)
        self.law = roll_dice(7)
        self.population = roll_dice(7)
        self.power = roll_dice(7)
        self.wealth = roll_dice(7)
        self.first_founding = determine_first_founding()
        self.historical_events_int = determine_number_historical_events(self.first_founding)
        self.historical_events_str = determine_historical_events(self.historical_events_int)

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

        # Apply historical event modifiers
        for event in self.historical_events_str:
            self.apply_event_modifiers(event)

    def apply_event_modifiers(self, event):
        if event == "Doom":
            self.defense -= roll_dice(2)
            self.influence -= roll_dice(2)
            self.lands -= roll_dice(2)
            self.law -= roll_dice(2)
            self.population -= roll_dice(2)
            self.power -= roll_dice(2)
            self.wealth -= roll_dice(2)
        elif event == "Defeat":
            self.defense -= roll_dice(1)
            self.influence -= roll_dice(1)
            self.lands -= roll_dice(1)
            self.law -= 0
            self.population -= roll_dice(1)
            self.power -= roll_dice(1)
            self.wealth -= roll_dice(1)
        elif event == "Catastrophe":
            self.law -= roll_dice(1)
            self.population -= roll_dice(1)
            self.power -= roll_dice(1)
            self.wealth -= roll_dice(1)
        elif event == "Madness":
            self.defense += (6 - roll_dice(2))
            self.influence += (6 - roll_dice(2))
            self.lands += (6 - roll_dice(2))
            self.law += (6 - roll_dice(2))
            self.population += (6 - roll_dice(2))
            self.power += (6 - roll_dice(2))
            self.wealth += (6 - roll_dice(2))
        elif event == "Invasion/Revolt":
            self.law -= roll_dice(2)
            self.population -= roll_dice(1)
            self.power -= roll_dice(1)
            self.wealth -= roll_dice(1)
        elif event == "Scandal":
            self.influence -= roll_dice(1)
            self.lands -= roll_dice(1)
            self.power -= roll_dice(1)
        elif event == "Treachery":
            self.influence -= roll_dice(1)
            self.law -= roll_dice(1)
            self.power += roll_dice(1)
        elif event == "Decline":
            self.influence -= roll_dice(1)
            self.lands -= roll_dice(1)
            self.population -= roll_dice(1)
            self.power -= roll_dice(1)
            self.wealth -= roll_dice(1)
        elif event == "Infrastructure":
            # Choose two attributes and increase each by +roll_dice(1)
            attributes_to_increase = random.sample(
                ["defense", "influence", "lands", "law", "population", "power", "wealth"], 2)
            for attr in attributes_to_increase:
                setattr(self, attr, getattr(self, attr) + roll_dice(1))
        elif event == "Ascent":
            self.influence += roll_dice(1)
            self.lands += roll_dice(1)
            self.power += roll_dice(1)
            self.wealth += roll_dice(1)
        elif event == "Favor":
            self.influence += roll_dice(1)
            self.lands += roll_dice(1)
            self.law += roll_dice(1)
            self.power += roll_dice(1)
        elif event == "Victory":
            self.defense += roll_dice(1)
            self.influence += roll_dice(1)
            self.power += roll_dice(1)
        elif event == "Villain":
            self.influence += roll_dice(1)
            self.law -= roll_dice(1)
            self.population -= roll_dice(1)
            self.power += roll_dice(1)
        elif event == "Glory":
            self.defense += roll_dice(1)
            self.influence += roll_dice(1)
            self.law += roll_dice(1)
            self.power += roll_dice(1)
        elif event == "Conquest":
            self.defense -= roll_dice(1)
            self.influence += roll_dice(1)
            self.lands += roll_dice(1)
            self.law -= roll_dice(1)
            self.population += roll_dice(1)
            self.wealth += roll_dice(1)
        elif event == "Windfall":
            self.defense += roll_dice(1)
            self.influence += roll_dice(2)
            self.lands += roll_dice(1)
            self.law += roll_dice(1)
            self.population += roll_dice(1)
            self.power += roll_dice(2)
            self.wealth += roll_dice(2)

    def get_house_stats(self):
        return {
            "defense": self.defense,
            "influence": self.influence,
            "lands": self.lands,
            "law": self.law,
            "population": self.population,
            "power": self.power,
            "wealth": self.wealth,
        }

    def __str__(self):
        description = [
            f"- Location: {self.location}",
            f"- First Fouding: {self.first_founding}",
            f"- Historical events: {self.historical_events_str}",
            f"- Defense: {self.defense} / {describe_defense_score(self.defense)}",
            f"- Influence: {self.influence} / {describe_influence_score(self.influence)}",
            f"- Lands: {self.lands} / {describe_lands_score(self.lands)} ",
            f"- Law: {self.law} / {describe_law_score(self.law)}",
            f"- Population: {self.population} / {describe_population_score(self.population)}",
            f"- Power: {self.power}  / {describe_power_score(self.power)}",
            f"- Wealth: {self.wealth}   / {describe_wealth_score(self.wealth)}"
        ]
        return "\n".join(description)


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


def describe_defense_score(defense):
    if defense == 0:
        return "Desolate, ruined land, ravaged by disaster, war, or simply abandoned. No defensible structures of any kind, and no infrastructure for moving troops. You have no fortifications whatsoever."
    elif 1 <= defense <= 10:
        return "Scarce cultivation, mostly wilderness with a few unprotected pockets of civilization, having one or two roads or a minor stronghold."
    elif 11 <= defense <= 20:
        return "Some cultivation, presence of a keep or smaller stronghold with a few roads, rivers, or ports."
    elif 21 <= defense <= 30:
        return "Defensible, with at least one fortified town or castle. Roads and trails are present, and rivers or ports are likely."
    elif 31 <= defense <= 40:
        return "Good defenses with, almost certainly, a castle, along with a few other strong points. Roads and rivers provide easy transportation. Alternatively, natural terrain features, such as mountains or swamps, provide additional fortification."
    elif 41 <= defense <= 50:
        return "Excellent defenses, with man-made fortifications likely combined with defensible terrain features."
    elif 51 <= defense <= 60:
        return "Extraordinary defenses with structures, walls, and terrain features that, when combined, make attacking this land very costly."
    elif 61 <= defense <= 70:
        return "Among the greatest defenses in the world. A good example would be the Eyrie and the Vale of Arryn."
    else:
        return "Unknown Defense Score"  # Handle any other value not in the specified range


def describe_influence_score(influence):
    if influence == 0:
        return "The house’s name and history has been erased from all records, and no one speaks of them anymore."
    elif 1 <= influence <= 10:
        return "Maximum Lord's Status 2. A minor landed knight or the equivalent. An example would be Craster."
    elif 11 <= influence <= 20:
        return "Maximum Lord's Status 3. A greater landed knight or the equivalent. A sample house would include the Knotts and Liddles of the North."
    elif 21 <= influence <= 30:
        return "Maximum Lord's Status 4. A small minor house. Examples include House Mormont and House Westerling."
    elif 31 <= influence <= 40:
        return "Maximum Lord's Status 4. A minor house. Examples include House Clegane, House Payne, and House Karstark."
    elif 41 <= influence <= 50:
        return "Maximum Lord's Status 5. A powerful minor house with a colorful history. Examples include House Florent and House Frey."
    elif 51 <= influence <= 60:
        return "Maximum Lord's Status 6. A major house. Examples include House Tully and House Martell."
    elif 61 <= influence <= 70:
        return "Maximum Lord's Status 7. A great house. Examples include House Arryn, House Stark, House Baratheon, and House Lannister."
    else:
        return "Unknown Influence Score"  # Handle any other value not in the specified range


def describe_lands_score(lands):
    if lands == 0:
        return "Landless, the house has been completely stripped of its holdings."
    elif 1 <= lands <= 10:
        return "A speck of land, no larger than a single town."
    elif 11 <= lands <= 20:
        return "A small stretch of land, about the size of a single small island or small portion of a larger island, or a large city and its immediate environs, such as House Mormont."
    elif 21 <= lands <= 30:
        return "A modest stretch of land or medium-size island, such as House Frey."
    elif 31 <= lands <= 40:
        return "An area of land that includes several terrain features, islands, or large groups of islands, House Greyjoy for example."
    elif 41 <= lands <= 50:
        return "A large area of land, that spreads across a great distance. This area likely includes a variety of terrain features. House Martell’s control of Dorne is representative of this level of resource."
    elif 51 <= lands <= 60:
        return "A huge area of land representing a considerable portion of Westeros’ geography. House Stark’s command of the North is a good example."
    elif 61 <= lands <= 70:
        return "Most, if not all, of the Seven Kingdoms, such as the holdings of King Robert and the royal branch of House Baratheon."
    else:
        return "Unknown Lands Score"  # Handle any other value not in the specified range


def describe_law_score(law):
    if law == 0:
        return "Lawless, uncivilized land. You have no authority here—the lands beyond the Wall."
    elif 1 <= law <= 10:
        return "Bandits, raiders, and other criminal bands are afoot in your lands, causing mischief and trouble."
    elif 11 <= law <= 20:
        return "Lawlessness and banditry are a problem along the fringes of your lands."
    elif 21 <= law <= 30:
        return "The typical level of Law throughout much of Westeros. Crime is common but not out of control."
    elif 31 <= law <= 40:
        return "You exert a great deal of control over your lands, and crime is uncommon."
    elif 41 <= law <= 50:
        return "Such is your influence and devotion to maintaining the peace that crime is rare."
    elif 51 <= law <= 60:
        return "You have almost no crime at all in your lands."
    elif 61 <= law <= 70:
        return "There is no crime in your lands."
    else:
        return "Unknown Law Score"  # Handle any other value not in the specified range


def describe_power_score(power):
    if power == 0:
        return "Powerless, you have no troops, no soldiers, and none loyal to your family."
    elif 1 <= power <= 10:
        return "Personal guard only, with one or two sworn swords and a cadre of smallfolk warriors at most."
    elif 11 <= power <= 20:
        return "Small force of soldiers largely made up of smallfolk."
    elif 21 <= power <= 30:
        return "A modest force of soldiers, including some trained troops."
    elif 31 <= power <= 40:
        return "A trained force of soldiers, including cavalry and possibly ships. You may have the service of a banner house."
    elif 41 <= power <= 50:
        return "A large force of diverse, trained, and competent soldiers. You probably also have the services of a small navy as well. Several banner houses are sworn to you."
    elif 51 <= power <= 60:
        return "You can muster a huge force of soldiers, drawn from your lands and those from your numerous banner houses."
    elif 61 <= power <= 70:
        return "You have the strength of most of the Seven Kingdoms behind you."
    else:
        return "Unknown Power Score"  # Handle any other value not in the specified range


def describe_population_score(population):
    if population == 0:
        return "Barren. No people live under your rule."
    elif 1 <= population <= 10:
        return "Thinly populated. Tiny settlements are scattered throughout your lands."
    elif 11 <= population <= 20:
        return "Small population but no single community larger than a small town."
    elif 21 <= population <= 30:
        return "Typical population. Most smallfolk live on farmsteads or in hamlets, but you might have a couple of small towns and a community around your primary fortification."
    elif 31 <= population <= 40:
        return "Modest population. At least one town and several small hamlets."
    elif 41 <= population <= 50:
        return "Large population. You have a large number of people in your lands; many live in a large town or spread throughout a number of smaller towns."
    elif 51 <= population <= 60:
        return "Immense population. An enormous number of people live under your protection."
    elif 61 <= population <= 70:
        return "All or nearly all of Westeros."
    else:
        return "Unknown Population Score"  # Handle any other value not in the specified range


def describe_wealth_score(wealth):
    if wealth == 0:
        return "Destitute. Your family is penniless."
    elif 1 <= wealth <= 10:
        return "Impoverished. Your family lacks essential resources and struggles to make ends meet."
    elif 11 <= wealth <= 20:
        return "Poor. Your family has little excess. While they are able to sustain themselves and their holdings, they do not live in luxury."
    elif 21 <= wealth <= 30:
        return "Common. Your family has enough to get by."
    elif 31 <= wealth <= 40:
        return "Prosperous. Your family has the funds to live in accordance with their station."
    elif 41 <= wealth <= 50:
        return "Affluent. Your family has more funds than it needs and lives in comfort."
    elif 51 <= wealth <= 60:
        return "Rich. Your family wants for nothing."
    elif 61 <= wealth <= 70:
        return "Decadent. Your family is so wealthy, they can afford to have seventy-seven course feasts."
    else:
        return "Unknown Wealth Score"  # Handle any other value not in the specified range


def determine_number_historical_events(first_founding):
    if first_founding == "Ancient Age of Heroes":
        return random.randint(1, 6) + 3
    elif first_founding == "Very Old Andal Invasion":
        return random.randint(1, 6) + 2
    elif first_founding == "Old Rhoynar Invasion":
        return random.randint(1, 6) + 1
    elif first_founding == "Established Aegon’s Conquest":
        return random.randint(1, 6)
    elif first_founding == "Recent Blackfyre Rebellion":
        return max(random.randint(1, 6) - 1, 0)
    elif first_founding == "New War of the Usurper":
        return max(random.randint(1, 6) - 2, 0)
    else:
        return 0  # Handle any other value not in the specified list


# Example usage to determine historical events for a specific First Founding

def determine_first_founding():
    roll = random.randint(1, 6)
    if roll == 1:
        return "Ancient Age of Heroes"
    elif roll == 2:
        return "Very Old Andal Invasion"
    elif roll == 3:
        return "Old Rhoynar Invasion"
    elif roll == 4:
        return "Established Aegon’s Conquest"
    elif roll == 5:
        return "Recent Blackfyre Rebellion"
    elif roll == 6:
        return "New War of the Usurper"
    else:
        return "Unknown First Founding"  # Handle any other roll value not in the specified range


def determine_historical_events(number_historical_events):
    event_results = [roll_dice(3) for _ in range(1, number_historical_events)]
    historical_events = []

    for result in event_results:
        if result == 3:
            historical_events.append("Doom")
        elif result == 4:
            historical_events.append("Defeat")
        elif result == 5:
            historical_events.append("Catastrophe")
        elif result == 6:
            historical_events.append("Madness")
        elif result == 7:
            historical_events.append("Invasion/Revolt")
        elif result == 8:
            historical_events.append("Scandal")
        elif result == 9:
            historical_events.append("Treachery")
        elif result == 10:
            historical_events.append("Decline")
        elif result == 11:
            historical_events.append("Infrastructure")
        elif result == 12:
            historical_events.append("Ascent")
        elif result == 13:
            historical_events.append("Favor")
        elif result == 14:
            historical_events.append("Victory")
        elif result == 15:
            historical_events.append("Villain")
        elif result == 16:
            historical_events.append("Glory")
        elif result == 17:
            historical_events.append("Conquest")
        elif result == 18:
            historical_events.append("Windfall")

    return historical_events


# Example usage for a House
house = House()
print(str(house))
