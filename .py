from model import Pokemon
from model import Attack

x = Pokemon.Pokemon(50,"t",100,"grass",[],100,1,1,1,1)
y = Pokemon.Pokemon(50,"j",100,"water",[],1,100,1,1,1)
at = Attack.Attack("grass","attack","special",100,power=80)

print(y.health)
x.attack(at,y)
print(y.health)