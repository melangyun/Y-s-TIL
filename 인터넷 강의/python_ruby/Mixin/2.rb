class Cal
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
    
    class CalMultiply < Cal
        def multiply()
            return @v1 * @v2
        end
    end
    
    c1 = CalMultiply.new(10,10)
    p c1. add()
    p c1. multiply