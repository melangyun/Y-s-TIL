def recursive(data):
    if data < 0:
        print("end")
    else:
        print(data)
        recursive(data -1)
        print ("returned", data)

recursive(4)
# ! 실행시카면 아래와 같이 출력된다.
# 4
# 3
# 2
# 1
# 0
# end
# returned 0
# returned 1
# returned 2
# returned 3
# returned 4

# ? 왜 ?
# ? Process Stack 에 아래와 같이 쌓여있다. 따라서 스택에 쌓인 재귀함수를 끝내고 "return"이 불려지게 된다.
# recursive(-1)
# recursive(0)
# recursive(1)
# recursive(2)
# recursive(3)
# recursive(4)

# ! 더 공부하고 싶다면 운영체제 과목을 공부할것
# process stack, 이 이러한 Stack 구조를 기반으로 만들어 져있다.


# ! 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기

data_stack = list()

def push(data):
    data_stack.append(data)

def pop(data):
    # * 0번은 가장 앞, -1은 가장 뒤임!
    data = data_stack[-1]
    return data

for index in range(10):
    push(index)

print(pop(data_stack))