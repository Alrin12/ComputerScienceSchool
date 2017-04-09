from abc import *

class Character(metaclass = ABCMeta):
    def __init__(self):
        self.hp = 100
        self.attack_power = 20
        
    def attack(self, other, attack_kind):
        other.get_damage(self.attack_power, attack_kind)

    @abstractmethod
    def get_damage(self, attack_power, attack_kind):
        pass




if __name__ == "__main__":
    #error 확인!
    c1 = Character("oger")
    
