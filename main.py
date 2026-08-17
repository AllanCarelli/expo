from controller.app import main
from model.Attack import Attack
from model.Pokemon import Pokemon

def webpage():
    main()


def game():
    grama = Attack("grass","attack","physical",100,power=40)
    bulba = Pokemon(15,"Bulba",100,"grass",[],10,10,10,10,10)
    char = Pokemon(15,"Char",100,"fire",[],10,10,10,10,10)
    bulba.attack(grama,char)

game()
