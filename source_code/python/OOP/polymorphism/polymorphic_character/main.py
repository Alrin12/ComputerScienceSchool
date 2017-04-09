from player import Player
from monster import *

if __name__ == "__main__":
    play = Player()

    monsters = []
    monsters.append(IceMonster())

    monsters.append(FireMonster())

    print("*" * 5 + "before a player attacks monsters" + "*" * 5)
    
    for monster in monsters:
        print(monster)

    for monster in monsters:
        play.attack(monster, "ICE")

    print("\n\n")
    print("*" * 5 + "after a player attacks monsters" + "*" * 5)
    
    for monster in monsters:
        print(monster)
        
    
    
