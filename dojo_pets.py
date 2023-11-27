class Pet():
    # health = 0
    # energy = 0
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0

    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health +=5
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print("pet's sound")
        return self

class Ninja():
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food 
    
    def walk(self, pet):
        self.pet.play()
        print(pet.health)
        print(pet.energy)
        return self
    
    def feed(self):
        self.pet.eat()
        # print(self.pet.health)
        # print(self.pet.energy)
        return self    
    
    def bathe(self, pet):
        self.pet.noise()
        print(pet.health)
        print(pet.energy)
        return self
    
bob = Pet("bob", "dog", "spin")
red_ninja = Ninja("john", "doe", bob, "bacon", "kibble")
# red_ninja.pet = bob

red_ninja.feed()
# red_ninja.walk(bob)
# red_ninja.bathe(bob)
print(bob.health)
print(bob.energy)