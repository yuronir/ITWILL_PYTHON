from abc import ABCMeta, abstractmethod

class animal(metaclass=ABCMeta):
    # __metaclass__ = ABCMeta # 추상 클래스로 선언

    @abstractmethod # 추상 메소드 선언
    def bark(self):
        pass

class dog(animal):
    pass
    # def bark(self):
    #     print('멍멍')

class cat(animal):
    def __init__(self):
        self.sound = '야옹 !'

    def bark(self):
        print(self.sound)

dog1 = dog()
cat1 = cat()
cat1.bark()