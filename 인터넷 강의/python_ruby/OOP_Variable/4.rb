class C
    # attribute 속성
    # ? value의 직접접근을 위해 attribute로 지정함
    attr_reader :value
    # ? 속성쓰기가능 지정
    attr_writer :value

    # ! 둘다 가능하게 하려면
    # ! attr_accessor :value

    def initialize(v)
        @value = v
    end

    def getValue()
        return @value
    end

    def setValue(v)
        @value = v
    end
end

c1 = C.new(10)
# * 읽기 가능
p c1.value

c1.value = 20
p c1.value

#!  읽기 전용 데이터를 하기 위해서
