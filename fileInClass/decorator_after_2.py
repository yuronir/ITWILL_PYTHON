def is_admin(func):
    # *arg 리스트의 가변 매개변수
    # **kwargs 딕셔너리 가변 매개변수
    def wrapper(*args,**kwargs):
        if kwargs.get('name') != 'admin':
            raise Exception("권한이 없어요")
        return func(*args,**kwargs)
    return wrapper

class Greet(object):
    current_user = None #current_user라는 변수 선언

    @is_admin
    def set_name(self,name):
        #name에 admin이 들어오면 current_user를 admin으로 변경
        self.current_user = name

    @is_admin
    def get_greeting(self,name):
        #name이라는 매개변수에 admin이 입력됐다면 Hello와 current_user를 리턴하는 함수수
        return "Hello {}".format(self.current_user)

greet = Greet()
greet.set_name(name='admin')
greet.set_name(name='admin')