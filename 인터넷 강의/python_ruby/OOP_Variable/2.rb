class C
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
p c1.getValue()

c1.setValue(20)
p c1.getValue()