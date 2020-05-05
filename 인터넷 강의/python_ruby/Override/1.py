class C1:
    def m(self):
        return "parent"


class C2(C1):
    # Override
    def m(self):
        # * C1의 m을 가르킨다. 
        # super().m()
        return super().m() + " child"
    # 메소드가 존재하지 않는 클래스는
    # ! "pass"키워드 사용
    pass

o = C2()
print(o.m())