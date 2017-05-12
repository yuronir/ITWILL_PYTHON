class Gun:
    bullet = 0

    @staticmethod
    def charge(count):
        Gun.bullet += count

    @staticmethod
    def shoot(count):
        for i in range(count):
            if Gun.bullet <= 0:
                print('잔탄이 부족합니다!')
            else:
                print('탕!')
                Gun.bullet -= 1

    @staticmethod
    def print():
        print("잔탄 : {0}발".format(Gun.bullet))

gun = Gun()
gun.shoot(3)