# Programming Paradigm

## 프로그래밍 패러다임은 프로그래머에게 프로그래밍의 관점을 갖게 해주고, 결정하는 역할을 한다.
- 객체 지향 프로그래밍은 프로그램을 상호작용하는 객체들의 집합으로 볼 수 있게 해준다.
- 함수형 프로그래밍은 상태값을 지니지 않는 함수 값들의 연속으로 생각할 수 있게 해준다.

## 프로그래밍 언어는 서로 다른 프로그래밍 패러다임을 지원한다.
- 스몰토크, jdk(1.8 이전) : 객체 지향 프로그래밍을 지원한다.
- 하스켈, 스킴 : 함수형 프로그래밍을 지원한다.
- 여러 프로그래밍 패러다임을 지원하는 언어도 있다. (커먼 리스프, 파이썬, 오즈, jdk 1.8 이상의 자바, c++)

## 프로그래밍 패러다임은 어떤 기법을 금지하거나 가능하게 한다.
- 순수 함수형 프로그래밍은 부작용의 사용을 허용하지 않는다.
    - 컴퓨터 과학에서 함수가 결과값 이이에 다른 상태를 변경시킬 때 부작용이 있다고 말한다.<br>
    예를 들어 함수가 전역변수나 정적변수를 수정하거나, 인자로 넘어온 것들 중 하나를 변경하거나, 화면이나 파일에 데이터를 쓰거나, 다른 부작용이 있는 함수에서 데이터를 읽어오는 경우가 있다.

    > 부작용은 프로그램의 동작을 이해하기 어렵게 한다.

    ### 부작용을 이용하는 함수는 참조에 불투명하다.

    - **참조에 투명한 함수(referentially opaque)**<br>
    참조에 투명한 함수는, 같은 인자를 주면 항상 같은 결과를 돌려주는 함수이다.
    ```ruby
        integer function rt(integer x)
        begin
            return x + 1;
        end
    ```
    - **참조에 불투명한 함수(referentially transparent)**<br>
    아래 코드는 파라미터 x의 값이 변한다면 return 되는 값이 변하므로, 참조에 불투명하다.
    ```ruby
        globalValue = 0 ;
        integer function rq(integer x)
        begin
            globalValue = globalValue + 1;
            return x + globalValue;
        end
    ```
    ### 부작용의 단점
    부작용은 프로그램의 버그가 발생하기 쉽다.<br>프로그램을 테스트할때에는 발생하지 않았던 예외 상황들이 프로그램을 사용하면서 발견되지만 항상 일어나지 않는 예외 상황이 일어나서 버그를 고치기 어렵게 하기도 한다.
- 구조적 프로그래밍은 `goto`문의 사용을 제한한다.


# 소프트웨어 개발 방법론
소프트웨어 개발 방법론은 소프트웨어를 생산하는 데에 필요한 프로그래밍 개발 과정들을 정리하고 표준화하여 프로그래머들이 프로그래밍 개발과정에서 각개인이 개발과정에서의 일관성을 유지하고 프로그래머들간의 효과적인 협업이 이루어질수 있도록 돕기 위한 방법론이다.
