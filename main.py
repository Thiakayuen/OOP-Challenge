
from Pet import pet

myPet = pet("Rockie")

# call functions to demonstrate basic interactions
print(" Basic Interactions ")
myPet.eat()
myPet.play()
myPet.sleep()
myPet.get_status()

# call training functions to demonstrate training
print("\n Training Tricks ")
myPet.train("cooking")
myPet.train("Learnt to code")
myPet.train("Bigging")
myPet.show_tricks()

# Show status after training
print("\n Final Status: ")
myPet.get_status()