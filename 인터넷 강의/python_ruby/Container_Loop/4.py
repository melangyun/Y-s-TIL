input_id = input("아이디를 입력해주세요 : ")

members = ['egoing', 'k880']
for member in members:
    if member == input_id:
        print('Hello,! '+ member)
        import sys
        sys.exit()
print("Who are you?")