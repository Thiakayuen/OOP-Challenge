class Pet:
    def __init__(self, name):
        """
        Initialize a new pet with a name and default attributes:
        hunger: 5 (moderately hungry)
        energy: 5 (moderately rested)
        happiness: 5 (moderately happy)
        tricks: empty list for learned tricks
        """
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []  # for bonus
