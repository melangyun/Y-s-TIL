# print("아이디를 입력해주세요 : ")
# input_id = gets.chomp()

# members = ['egoing', 'k880']
# for member in members do
#     if member == input_id
#         puts("Hello," + member)
#         exit
#     end
# end
# puts("Who are you?")

print("아이디를 입력해주세요 : ")
input_id = gets.chomp()

def login(id)
    members = ['egoing', 'k880', 'leezche']
    for member in members do
        if member == id
            return true
        end
    end
    return false
end

if login(input_id)
    puts("Hello, " + input_id)
else
    puts("who are you?")
end