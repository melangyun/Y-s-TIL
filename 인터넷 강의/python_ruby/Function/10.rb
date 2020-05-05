arr = [1,3, 56, 7, 13, 52 ]
arr.delete_if(){|item| 
    item > 7
}

# 위와 같은 코드이다.
arr.delete_if() do |item| 
    item > 7
end

# 1, 3, 7 만 남음
puts arr