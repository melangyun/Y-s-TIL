# ruby-doc.org

# Core API - 기본으로 있는것
# Standard Library API - import가 필요한것

arr = [1,2,3,4,5,6]
print("arr[2] : ",arr[2])
puts()

# index가 1인 원소부터 4개 반환해줌
print("arr[1..4] : ", arr[1..4])
puts()

# 인간 친화적으로 이런식으로도 작성 가능하다.
puts(arr.first)
puts(arr.last)

print("arr.length : ",arr.length)
puts()

arr = [1, 2, 3, 4 ]
print("arr puts : ",arr)
puts()
arr.push(5)
print("changed arr puts : ",arr)
puts()

# 인덱스에 해당하는 원소 삭제
arr.delete_at(2)
print("delete_at arr puts : ",arr)
puts()
