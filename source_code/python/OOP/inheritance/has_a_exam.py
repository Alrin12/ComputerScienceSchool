class Gun:
    def __init__(self, kind):
        self.kind = kind

    #총에서 총알이 발사되는 함수
    def bang(self):
        print("빵야~빵야")
        
#객체합성
class Police:
    def __init__(self, gun_kind = ''):
        if gun_kind:
            self.gun = Gun(gun_kind)
        else:
            self.gun = None  

    #총을 바꾸거나 총 없는 경찰에게 총이 주어질 때
    def get_gun(self, gun_kind):
        self.gun = Gun(gun_kind) 

    #경찰이 총을 쏘는 함수
    def shoot(self):
        if self.gun:
            self.gun.bang()
        else:
            print("너 총 없어. 못 쏴!")
            
if __name__ == "__main__":
    p1 = Police("리볼버")
    p1.shoot()

    #총이 없는 경찰 객체
    p2 = Police()
    p2.shoot()

    #총을 얻은 후
    p2.get_gun("기관총")
    #실제 발사한다
    p2.shoot()
    
    
