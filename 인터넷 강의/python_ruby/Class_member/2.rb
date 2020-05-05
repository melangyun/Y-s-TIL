class Cs
    #! Class method의 경우 Class Name이 반드시 기재되어야 한다.
    # ? instance 에서 class method를 호출하거나, Class에서 instance method를 호출한다면 에러가 발생한다.
    def Cs.class_method()
        p "Class method"
    end

    def instance_method()
        p "Instance method"
    end
end

i = Cs.new()
Cs.class_method()

i.instance_method()