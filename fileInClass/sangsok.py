class grandfather:
    def __init__(self):
        print("튼튼한 두 팔")

class father1(grandfather):
    def __init__(self):
        super().__init__()
        print("지식")

class father2(grandfather):
    def __init__(self):
        super().__init__()
        print("지혜")

class grandchild(father1,father2):
    def __init__(self):
        super().__init__()
        print("자기 만족도가 높은 삶")

grandchild = grandchild()