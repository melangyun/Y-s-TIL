class C
    def initialize(v)
        @value = v
    end

    def show()
        p @value
    end
end

c1 = C.new(10)

# !에러가 생성됨
# p c1.value
# p c1.value() 라고 생각하여
# value를 메소드라고 생각하기때문에 에러
# ? 인스턴스에 대한 접근을 (정책적으로도)허용하지 않음
