class C1
    def m()
        return "parent"
    end
end

class C2 < C1
    def m()
        # ! ruby에서 super는 현재 메소드에서의 같은 이름을 갖고있는 상위 클래스의 "메소드"를 가르킨다!
        return super() + " child"
    end
end

o = C2.new()
p o.m()