class Cal
    @@_history = []

    def initialize(v1, v2)
        @v1 = v1
        @v2 = v2
    end
    #! @가 붙으면 인스턴스 변수이다.

    def add()
        result = @v1 + @v2
        @@_history.push("#{@v1}  + #{@v2} = #{result}")
        return result
    end

    def subtract()
        result = @v1 - @v2
        @@_history.push("#{@v1}  - #{@v2} = #{result}")
        return result
    end

    def setV1(v)
        if v.is_a?(Integer)
            @v1 = v
        end
    end

    def getV1()
        return @v1
    end

    def Cal.history()
        for item in @@_history
            p item
        end
    end

end

class CalMultiply < Cal
    def multiply()
        result = @v1 * @v2
        @@_history.push("#{@v1}  * #{@v2} = #{result}")
        return result
    end
end

c1 = CalMultiply.new(10,10)
p c1. add()
p c1. multiply
CalMultiply.history()