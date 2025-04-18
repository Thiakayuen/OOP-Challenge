class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    # reduces hunger by 3 points (but not below 0), and increases happiness by 1.
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has eaten so hunger decreased,and happiness increased!")

    # increases energy by 5 points (but not above 10).
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} has slept so energy increased!")

    # decreases energy by 2, increases happiness by 2, and increases hunger by 1.
    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played and had fun! Energy decreased, happiness and hunger increased.")

    # that teaches your pet a new trick and stores it in a list.
    def train(self, trick):
        if self.energy >= 3:
            self.tricks.append(trick)
            self.energy -= 3
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned '{trick}'!")
        else:
            print(f"{self.name} is too tired to train right now.")
        

    def show_tricks(self):
        if not self.tricks:
             print(f"{self.name} doesn't know any tricks yet.")
        else:
            print(f"{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")

    # prints the current state of the pet.
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

my_pet = Pet("Buddy")

# call functions to demonstrate basic interactions
print(" Basic Interactions ")
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.get_status()

# call training functions to demonstrate training
print("\n Training Tricks ")
my_pet.train("cooking")
my_pet.train("Learnt to code")
my_pet.train("Bigging")
my_pet.show_tricks()

# Show status after training
print("\n Final Status: ")
my_pet.get_status()




# class Pet:
#     def __init__(self, name):
#         self.name = name
#         self.hunger = 5
#         self.energy = 5
#         self.happiness = 5
#         self.tricks = []

#     def eat(self):
#         self.hunger = max(0, self.hunger - 3)
#         self.happiness = min(10, self.happiness + 1)
#         print(f"{self.name} is eating...")

#     def sleep(self):
#         self.energy = min(10, self.energy + 5)
#         print(f"{self.name} is sleeping...")

#     def play(self):
#         if self.energy <= 0:
#             print(f"{self.name} is too tired to play.")
#             return
#         self.energy = max(0, self.energy - 2)
#         self.happiness = min(10, self.happiness + 2)
#         self.hunger = min(10, self.hunger + 1)
#         print(f"{self.name} is playing...")

#     def train(self, trick):
#         self.tricks.append(trick)
#         print(f"{self.name} learned a new trick: {trick}")

#     def show_tricks(self):
#         print(f"{self.name}'s tricks: {self.tricks if self.tricks else 'No tricks yet.'}")

#     def get_status(self):
#         print(f"{self.name}'s current status:")
#         print(f"Hunger: {self.hunger}")
#         print(f"Energy: {self.energy}")
#         print(f"Happiness: {self.happiness}")
#         self.show_tricks()
