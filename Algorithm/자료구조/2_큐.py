import queue

# ! 일반적인 큐!

# data_queue이름으로 queue 생성
data_queue = queue.Queue()
# queue 를 사용하면 FiFO 정책을 쓴 일반적인 큐 생성

# enqueue 라이브러리 에는 put으로 구현되어있음
data_queue.put("FunCoding")
data_queue.put(1)

size = data_queue.qsize()
print(size)

# 데이터를 꺼냄..FIFO -> 첫번째 것이 나오고, 인자는 업슴
print(data_queue.get())

print(data_queue.qsize())

# ! 변형된 큐
# LifoQueue() 큐
lifo_queue = queue.LifoQueue()

# 함수의 형태는 같음
lifo_queue.put("Funcoding")

lifo_queue.put(100)

print("lifo_queue.get() : ",lifo_queue.get())

# ! priorityQueue()로 큐 만들기
# 데이터를 넣는 순서가 아닌, 입력해 주었던 우선순위에 따라 outPut 나옴

priority_queue = queue.PriorityQueue()

# ? 튜플로 쌍으로 넣음
# (우선순위, 데이터)
# * 우선순위가 높은것은 우선순위 번호가 낮음!

# 우선순위 10번, 데이터 "korea"
priority_queue.put((10, "korea"))
# 우선순위 5번, 데이터 "1"
priority_queue.put((5, 1))
priority_queue.put((15, "china"))

# (5,1)이 출력됨
print(priority_queue.get())
# (5, 1 ) -> (10, "korea") -> (15 , "china")