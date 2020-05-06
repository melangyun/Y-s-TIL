class C1():
    def c1_m(self):
        print("c1_m")

    def m(self):
        print("C1 m")

class C2():
    def c2_m(self):
        print("c2_m")

    def m(self):
        print("C2 m")

# ! 아무런 메소드도 갖고 있지 않은 class 단, C1, C2를 상속받음
# * 앞쪽에 등장하는 class의 우선순위가 더 높음
class C3(C1, C2):
    pass

c = C3()
c.c1_m()
c.c2_m()

# c1 m이 출력됨
c.m()
# ? 따라서 다중상속을 사용하지 않는 것이 권장됨

# ! __mro__를 사용하면 class의 우선순위가 무엇인지 반환된다.
# (<class '__main__.C3'>, <class '__main__.C1'>, <class '__main__.C2'>, <class 'object'>)
print(C3.__mro__)