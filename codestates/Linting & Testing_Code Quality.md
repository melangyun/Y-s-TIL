# Linting & Testing_Code Quality

1. 작성한 코드가 의도한 대로 동작하는가?
2. 작성한 코드에 결함이나 문제가 없는가?
3. 작성한 코드가 읽기 쉽고 유지 보수가 용이한가?

- Linting & Testing을 통해 코드 퀄리티를 높일 수 있다!
- Linting is the process of running a program that will analyse code for potentail errors.
  Testing을 통해 의도대로 동작하는지, 결함 혹은 문제가 없는지 확인할 수 있다.



- Linter : 코드 스타일을 지키는지 체크해 주는 툴
  읽기 좋은 코드, 유지 보수하기 좋은 코드를 만드는데 큰 도움을 준다.
- Tester : 작성한 코드가 의도한 대로 동작하는지, 결함이 없는지 자동화하여 테스트 해주는 툴

## Testing Tool

1. End to End Test
2. Intetration Test
3. Unit Test

우리가 학습할 것은 Unit Test에 해당하는 Jest로, FaceBook에서 제작하였다.

## ESLint_JS Linint Untility

대부분의 프로그래밍 언어는 컴파일 하는 과정이 있어 컴파일 시 수행되는 Linter가 내장되어있다. 그러나, 역동적이고 느슨한 언어인 JS는 Linter가 존재하지 않는다. JS는 별도의 컴파일 과정이 없고 Node나 Browser에서 바로 실행되기 때문이다.
따라서, JS개발시 구문 오류나 기타 오류를 찾기 위해서는 실제 실행까지 시켜봐야 한다.
하지만, ESLint 같은 Linting도구를 사용하면 JS를 실행하지 않고도 기본적인 문제를 발견 할 수 있다.

### 사용환경

- ESLint를 사용 할 수 있는 환경은 두가지가 존재한다.
  1. JS개발시 사용되는 IDE/Editor에 지원되는 ESLint 플러그인 설치
  2. WebPack을 사용하여 Webpack번들링 시 Eslint-loader를 추가하여 사용

### 환경설정

ESLint 를 사용할 때 환경설정 파일이 존재한다.이 환경 설정 파일을 참고하여 Linter는 소스코드 체크를 수행한다. 환경 설정은 IDE/Editor에 따라서 별도의 UI로 제공되는 경우도 있고, 환경 설정 파일 내용을 오픈 소스로 공개하여 재신들만의 ESLint환경 설정을 배포하기도 한다.( Airbnb, naver...)

자신만의 Linting을 설정하고자 한다면, ESLint 공식 홈페이지에서 확인하여 설정할 수 있다.

## Prettier(프리티어)

- Lint 와 Prettier의 차이
  - Prettier : 코드의 모양을 설정
  - Lint : 정해놓은 대로 안쓰면 에러를 내버림.