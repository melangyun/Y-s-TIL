class Cs:

    # ! 클래스 변수는 이런식으로 선언함!
    count = 0

    def __init__(self):
        Cs.count = Cs.count + 1

    @classmethod
    def getCount(cls):
        print(cls)
        return Cs.count

i1 = Cs()
i2 = Cs()
i3 = Cs()

print(Cs.getCount())