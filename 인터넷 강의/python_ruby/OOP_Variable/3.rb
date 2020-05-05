# Class를 만들때의 키워드는 "class", 이름은 무조건 대문자여야함
class Cal
# 생성자 -> 인스턴스가 만들어질때 자동생성되는메소드
#? new로 인스턴스 생성할때 Initailize메소드로 생성됨
# @ 가 붙지않으면 지역변수    
    def initialize(v1, v2)
        @v1 = v1
        @v2 = v2
    end
    #! @가 붙으면 인스턴스 변수이다.

    def add()
        return @v1+@v2
    end

    def subtract()
        return @v1-@v2
    end

    def setV1(v)
        if v.is_a?(Integer)
            @v1 = v
        end
    end

    def getV1()
        return @v1
    end
end


c1 = Cal.new(10, 10)
# puts보다 더 자세히 출력해줌
p c1.add()
p c1.subtract()

c2 = Cal.new(30, 20)
c2.add()
c2.subtract()