from model import Attack
from model.TypeProcessor import return_mutliplier
import random


class Pokemon:
    """
    Class representation of a Pokemon.
    """
    def __init__(self, lvl: int, name: str, health: int, type: str, attacks: list, strength: int, defense: int, special_strength: int, special_defense: int, evasive: int = 100) -> None:
        self.lvl = lvl
        self.name = name
        self.health = health
        self.type = type
        self.attacks = attacks
        self.strength = strength
        self.defense = defense
        self.special_strength = special_strength
        self.special_defense = special_defense
        self.evasive = evasive

    def attack(self, attack: Attack, enemy: Pokemon) -> bool:
        """
        attack method that decides what to do with an given Attack Object.
        
        input:
        attack - Attack Object
        enemy - Pokemon Object
        
        output:
        bool - returns if sucessfull or not
        """
        if attack.use == "attack":
            return enemy.receive_damage(attack,self.strength)
        elif attack.use == "buff":
            return self.use_special(attack)
        elif attack.use == "nerf":
            return enemy.use_special(attack)
    
    def receive_damage(self, attack: Attack, enemy_strength: int) -> bool:
        """
        method that calculates the amount of damage received from an attack and then subtracts on its own health.

        input:
        attack - Attack Object
        enemy_strength - amount of strength that the Pokemon Object who called the method have

        output:
        bool - return if sucessfull or not
        """
        type_multiplier = return_mutliplier(attack,self.type)
        damage = ((2 * self.lvl / 5 + 2) * attack.power * (enemy_strength/self.defense)) / 50 + 2
        random_multiplier = random.choice([1,0.85,0.925])

        if random.randint(1,10)/10 <= attack.accuracy/self.evasive:
            self.health -= round(float(damage) * float(type_multiplier) * random_multiplier)
        else:
            print("Attack missed")
        return True

    def use_special(self, attack: Attack) -> bool:
        """
        calculates what atributes will be buffed by an special attack

        input:
        attack - Attack Object
    
        output:
        bool - returns if sucesssfull or not
        """
        if attack.special_atribute == "strength":
            self.strength *= attack.special_buff
        if attack.special_atribute == "defense":
            self.defense *= attack.special_buff
        if attack.special_atribute == "special_strength":
            self.special_strength *= attack.special_buff
        if attack.special_atribute == "special_defense":
            self.special_defense *= attack.special_buff
        if attack.special_atribute == "speed":
            self.speed *= attack.special_buff
        return True
        