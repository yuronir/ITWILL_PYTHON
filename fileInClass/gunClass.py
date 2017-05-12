class Gun:
    def __init__(self):
        self.bullet = 0

    def charge(self,count):
        self.bullet += count

    def shoot(self,count):
        for i in range(count):
            if self.bullet <= 0:
                print('잔탄이 부족합니다!')
            else:
                print('탕!')
                self.bullet -= 1

    def print(self):
        print("잔탄 : {0}발".format(self.bullet))


gun = Gun()
gun.charge(10)
gun.shoot(3)
gun.print()
gun.shoot(10)
gun.print()