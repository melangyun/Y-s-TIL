class Cs
    
    @@count = 0

    def initialize()
        # ! class 에 속한 변수는 "@"를 두개 붙이면 된다.
        @@count = @@count + 1
    end

    def Cs.getCount()
        @@count
    end

end

i1 = Cs.new()
i2 = Cs.new()
i3 = Cs.new()

p Cs.getCount()