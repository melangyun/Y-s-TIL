def f1()
    return "f1"
end

puts(f1())

# 루비에서는 함수의 괄호 생략 가능
def f2
    return 'f2'
end

puts(f2())


# 실행시에도 괄호 생략 가능
def f3
    return 'f3'
end

puts(f3)


def f4(a1)
    return a1
end
puts(f4("f4"))

# 괄호 생략 가능하지만, 한칸 띄우고 코딩해야함
def f5 a1
    return a1
end

puts(f5 "f5")

# 이런식으로도 괄호 없이 실행은 가능
puts f5 "f5"

# 매개변수 없이 실행 -> 생략
def f6
    return "f6"
end
puts f6

# return 도 생략이 가능하다.
def f7
    "f7"
end
puts f7

# 추가예제
def f8
    a = 1
    b = 2
    # 마지막에 등장한 값이 return값으로 간주된다.
    a + b 
end
# 정상적으로 출력됨
puts f8