class Greet(object):
    current_user = None #current_user라는 변수 선언

    def set_name(self,name):
        #name에 admin이 들어오면 current_user를 admin으로 변경
        if name == 'admin':
            self.current_user = name
        else:
            raise Exception("권한이 없네요")

    def get_greeting(self,name):
        #name이라는 매개변수에 admin이 입력됐다면 Hello와 current_user를 리턴하는 함수수
        if name == 'admin':
            return "Hello {}".format(self.current_user)


greet = Greet()
greet.set_name('admin')
print(greet.get_greeting('admin'))