import pandas as pd

#사원명을 입력하고 월급을 출력받는 함수
def find_sal2():
    try:
        emp = pd.DataFrame.from_csv('D:\data\emp_colname.csv')
        name = ''
        while name == '':
            name = input('월급을 알고 싶은 사원명을 입력하세요 : ')
        sal = emp['sal'][emp['ename']==name.upper()].values[0]
    except Exception as err:
        print('해당 사원은 없습니다.')
    else:
        print('월급 추출에 성공했습니다.')
        return sal

print(find_sal2())

##
#분자/분모를 입력하여 나눈 결과를 출력
def division():
    try:
        num1 = int(input('분자를 입력하세요 : '))
        num2 = int(input('분모를 입력하세요 : '))
        print((num1/num2))
    except ValueError:
        print('잘못된 입력입니다.')
        res = division()
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
        res = division()
    finally:
        print('나눈 값을 잘 추출했습니다.')
        return res

print(division())