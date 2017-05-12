#파이썬 함수의 4가지 특징
# 1. 변수에 할당할 수 있다.
def greet(name):
    return "Hello {}".format(name)

greet_someone = greet
print(greet_someone("scott")) #Hello scott

# 2. 다른 함수 내에서 정의될 수 있다.
def greeting(name):
    def greet_message():
        return 'Hello'
    return "{} {}".format(greet_message(),name)

print(greeting("scott")) #Hello scott

# 3. 함수의 인자(매개변수)값으로 전달할 수 있다.
def change_name_greet(func):
    name = "King"
    return func(name)

print(change_name_greet(greet)) #Hello King

# 4. 함수의 반환값이 될 수 있다.
#name을 받아 func을 실행하는데, 결과를 대문자로 바꾸어 출력
def uppercase(func):
    def wrapper(name):
        result = func(name)
        return result.upper()
    return wrapper

new_greet = uppercase(greet) #greet함수인데 대문자 출력 기능이 첨가된 버전
print(new_greet("scott")) #HELLO SCOTT

