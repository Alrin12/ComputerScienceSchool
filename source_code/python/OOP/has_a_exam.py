class Gun:
    def __init__(self, gun_kind):
        self.gunkind = gun_kind

class Policeman(Gun):
    def __init__(self, gun_kind = ''):
        self.gun = Gun(gun_kind)
        if not gun_kind:
            self.gun = None

if __name__ == "__main__":
    police_with_gun = Policeman("리볼버")
    print(police_with_gun.gun.gunkind)

    police_without_gun = Policeman()
    print(police_without_gun.gun)
    
