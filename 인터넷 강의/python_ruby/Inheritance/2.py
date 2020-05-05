class Cal(object):
    # 생성자의 첫번째 매개변수에 self를 놓아야한다
    # ! 생성자 keyword는 __init__이다.
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    # 메소드에 매개변수 self반드시 필요하다.
    def add(self):
        return self.v1 + self.v2

    def subtract(self):
        return self.v1 - self.v2

    def setV1(self, v):
        # 내장되어있는 instance인지 검사
        if isinstance(v, int):
            self.v1 = v
    
    def getV1(self):
        return self.v1


class CalMultiply(Cal):
    def multiply(self):
        return self.v1 * self.v2

c1 = CalMultiply(10, 10)
print(c1.multiply())