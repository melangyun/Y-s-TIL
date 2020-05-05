class C:
    def __init__(self, v):
        # ! 언더바 두개를 붙이면, 다른데에서 호출할때 호출되지 않음
        self.__value = v

    def show(self):
        print(self.__value)

c1 = C(10)

# ? 에러발생
#print(c1.__value)

c1.show()