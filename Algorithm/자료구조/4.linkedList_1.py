
# 시작 시의 node
class NodeEx:
    def __init__(self, data):
        self.data= data
        self.next = None

# class 의 method에서는 항상 self!
# 씰제 인자는 data 와 next (next의 default 는 none)
class Node:
    def __init__(self, data, next= None):
        self.data = data
        self.next = next

# ! Node와 Node연결하기 ( 포인터 활용 )

# 노드를 선언함
node1 = Node(1)
node2 = Node(2)

# 노드 1과 노드 2를 이음
node1.next = node2
# head를 node1로 저장, head의 주소는 갖고있어야 한다.
head = node1

# 새로운 인자 삽입
def add(data):
    node = head
    # node의 next가 없을때까지 반복
    while node.next:
        node = node.next
    node.next = Node(data)

# linked list 에 숫자를 넣음
for index in range(2,10):
    add(index)

node = head
while node.next:
    print(node.data)
    node = node.next
# 마지막 하나 Print
print (node.data)