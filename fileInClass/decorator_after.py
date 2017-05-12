import pandas as pd
emp = pd.read_csv("D:\data\emp_colname.csv")

class checkAuth:
    def __init__(self,f):
        self.func = f

    def __call__(self, *args, **kwargs):
        if args[0] != 'KING':
            raise Exception('안돼 못줘 돌아가')
        self.func(*args)

@checkAuth
def printSal(name):
    print(emp['sal'][emp['ename'] == name].values[0])

printSal('KING')
printSal('SCOTT')