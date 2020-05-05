# 5라는 정수에 속해있는 times를 실행시킴
5.times() {puts "5times"}
2.times() {puts "2times"}

# 3-> 5까지 올라가면서 3번 실행시킬것
# i는 블럭이 실행될때 마다 i변수 값이 변할것임
# 3부터 5까지 출력됨
3.upto(5){|i| puts "3 to 5 upto", i}