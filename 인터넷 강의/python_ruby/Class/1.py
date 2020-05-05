# class이름이 무조건 대문자일 필요는 없음
# class 이름 뒤 (object)가 와야한다.
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


c1 = Cal(10, 10)
print(c1.add())
print(c1.subtract())

c2 = Cal(30,20)
print(c2.add())
print(c2.subtract())