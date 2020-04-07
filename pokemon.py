#Pokemon class allows for pokemon to be created.
class Pokemon:
#Takes in inital values of pokemon and sets them to attributes. Current health has a default of 20 and knocked out has a default of false.
    def __init__(self, name, level, poke_type, max_health, current_health = 20, knocked_out = False):
        self.name = name 
        self.level = level 
        self.type = poke_type
        self.max_health = max_health
        self.health = current_health
        self.is_knocked_out = knocked_out
#if pokemon is called without attribute this returns the info about the pokemon.
    def __repr__(self):
        return ("{name} is a level {level}, {type} type pokemon. It is currently at {health} health, and has a max health of {maxhealth}.".format(name = self.name, level = self.level, type= self.type, health= self.health, maxhealth= self.max_health))
#method that lowers the health of the pokemon object. If the damage is greater than the pokemon's health then the pokemon gets knocked out.
    def lose_health(self, damage):
        new_health = self.health - damage
        if new_health >0:
            self.health = new_health 
            print("{name} has lost {damage} health! {name} now has {health} health.".format(name= self.name, damage = damage, health = self.health))
        elif new_health <= 0:
            self.health = 0
            self.is_knocked_out = True
            print(self.name + " has been knocked out!")
#method restores pokemon object to max health and sets knocked out to False.
    def revive(self):
        if self.is_knocked_out == True:
            self.is_knocked_out = False
            self.health = self.max_health
            print(self.name + " has been revived!")
#restores pokemon to full health    
    def restore_max_health(self):
        self.health = self.max_health
        print(self.name + " has been restored to full health.")
#method adds to the health of the object pokemon. Cannot add more health than the max health for the pokemon.
    def gain_health(self, gain_amount):
        new_health = self.health + gain_amount
        if new_health < self.max_health:
            self.health = new_health
            print("{name} has gained {gain} health! {name} now has {health} health.".format(name = self.name, gain = gain_amount, health = self.health))
        elif new_health <= self.max_health:
            self.health = self.max_health
            print(self.name + " has been restored to full health!")
#Simmilar to attack, this knocks out the OPPONENT'S pokemon, not the pokemon calling the attribute.
    def knock_out(self, other_pokemon):
        other_pokemon.health = 0 
        other_pokemon.is_knocked_out = True
        print(other_pokemon.name + " has been knocked out!")
#Simmilar to knock_out, this deals damage to the OPPONENT'S pokemon. Damage is based off of the type of the pokemon and the level.
    def attack(self, other_pokemon):
        if self.is_knocked_out != True:
            damage = 0 
            if self.type == "fire":
                if other_pokemon.type == "fire":
                    damage = 1/2 * self.level
                if other_pokemon.type == "water":
                    damage = 1/2 * self.level
                if other_pokemon.type == "grass":
                    damage = 2 * self.level
            if self.type == "water":
                if other_pokemon.type == "fire":
                    damage = 2 * self.level
                if other_pokemon.type == "water":
                    damage = 1/2 * self.level
                if other_pokemon.type == "grass":
                    damage = 1/2 * self.level
            if self.type == "grass":
                if other_pokemon.type == "fire":
                    damage = 1/2 * self.level
                if other_pokemon.type == "water":
                    damage = 2 * self.level
                if other_pokemon.type == "grass":
                    damage = 1/2 * self.level
            other_pokemon.lose_health(damage)
            print( "{selfname} has dealt {othername} {damage} damage!".format(selfname= self.name, othername= other_pokemon.name, damage = damage))
        else:
            print (self.name + " is knocked out and cannot attack.")
#Trainer class allows for trainers to be created.
class Trainer:
    def __init__(self, name, pokemon, potions, active_pokemon):
        self.name = name
        self.pokemons = pokemon
        self.potions = potions
        self.active_pokemon = active_pokemon
    def __repr__(self):
        return "The trainer {name} has {pokemon} pokemon, {potions} potions, and {active} is the active pokemon.".format(name = self.name, pokemon = self.pokemons, potions = self.potions, active = self.active_pokemon)
#method restores max health (or 1,000,000,000 health capping out at the max health of the specific pokemon) to the trainer's ACTIVE POKEMON. CANNOT REVIVE A KNOCKED OUT POKEMON THAT HAS BEEN SWITCHED OUT OF ACTIVE POKEMON. 
    def potion(self):
        self.potions = self.potions - 1
        if self.active_pokemon.is_knocked_out == False:
            self.active_pokemon.restore_max_health()
            print(self.name + " has restored " + self.active_pokemon + " to full health.")
        elif self.active_pokemon.is_knocked_out == True:
            self.active_pokemon.revive()
            print("{name} has revived {poke}".format(name= self.name, poke= self.active_pokemon))
#method used by trainer takes their active pokemon and attacks the OPPONENT TRAINER dealing damage to the opponent's active pokemon.
    def attack(self, other_trainer):
        their_pokemon = other_trainer.active_pokemon
        self.active_pokemon.attack(their_pokemon)
        print(self.name + " has attacked " + other_trainer.name +"!")
#simmilar to trainer.attack, this method knocks out the opponent's active pokemon.
    def knock_out_pokemon(self, other_trainer):
        their_pokemon = other_trainer.active_pokemon
        self.active_pokemon.knock_out(their_pokemon)
        print(self.name + " has attacked " + other_trainer.name +"!")
#method allows for trainer to switch their active pokemon to another pokemon in their belt as long as it is not knocked out.    
    def switch_active_pokemon(self, new_active_pokemon):
        for poke in self.pokemons:
            if poke == new_active_pokemon:
                if new_active_pokemon.is_knocked_out != True:
                    self.active_pokemon = new_active_pokemon
                    print(self.name + " has changed active pokemon to " + self.active_pokemon.name)

#Making your Pokemon and Trainers. pokemon = name, level, type, max health. Max health is the pokemon's level * 10. trainer = name, list of pokemon, # of potions, active pokemon.
#Examples: pok1 = Pokemon("pok1", 2, "fire", 20)     trainer1 = Trainer("trainer1", [pok1, pok3, pok6], 4, pok3)
pok1 = Pokemon("pok1", 2, "fire", 20)
pok2 = Pokemon("pok2", 3, "water", 30)
pok3 = Pokemon("pok3", 4, "grass", 40)
pok4 = Pokemon("pok4", 4, "fire", 40)
pok5 = Pokemon("pok5", 2, "water", 20)
pok6 = Pokemon("pok6", 3, "grass", 30)
trainer1 = Trainer("trainer1", [pok1, pok3, pok6], 4, pok3)
trainer2 = Trainer("trainer2", [pok2, pok4, pok5], 4, pok4)

#Playing Pokemon!

trainer1.attack(trainer2)
trainer2.attack(trainer1)
trainer1.attack(trainer2)
trainer1.attack(trainer2)
trainer1.attack(trainer2)

trainer1.knock_out_pokemon(trainer2)

trainer2.potion()

print(trainer2)