class C:
    def __init__(self, v):
        self.value = v
    def getValue(self):
        return self.value
    def setValue(self, v):
        self.value= v

c1 = C(10)
print(c1.getValue())
c1.setValue(20)
print(c1.getValue())
# ? 인스턴스 변수에 대한 접근을 허용함