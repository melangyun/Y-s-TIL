# Authentication and Full Stack Development

- 회원 가입 및 로그인, 로그아웃 기능 구현, 인증(authentication)
- 클라이언트, 서버, DB 모두를 다루면서, Full Stack 개발 환경에서의 전체적 흐름 및 작동을 직접 확인

****

- 사용자의 민감한 정보를 안전하게 저장할 수 있는 다양한 방법들을 익힌다.
- 암호화와 hashing, salting 등의 개념을 이해할 수 있다.
- 권한 부여(Authorization)과 인증(Authentication)에 대해 이해할 수 있다.
- 쿠키 혹은 세션을 통해 인증 구현을 할 수 있다.
- 클라이언트, 서버, DB전체 동작을 이해 할 수 있다.

# Urclass

## Hashing

어떠한 문자열에 '임의의 연산'을 적용하여 다른 문자열로 변환하는 것
ex_ SHA1

1. 모든 값에 대해 해시 값을 계산하는데 오래걸리지 않아야한다.
2. 최대한 해시 값을 피해야하며, 모든 값은 고유한 해시 값을 가진다.
3. 아주 작은 단위의 변경이라도 완전히 다른 해시 값을 가져야 한다.

### Encryption

암호화는 일련의 정보르 임의의 방식을 사용하여 다른 형태로 변환하여 해당 방식에 대한 정보를 소유한 사람을 제죄하고 이해할 수 없도록 '알고리즘;을 이용해 정보를 전달하는 과정 

### Salt

**해시하려는 값(원본)에 추가하는 값**

1. 암호화를 진행했다면, '해당 알고리즘을 알고있는 순간' 바로 원본을 얻어낼 수 있다.

2. 원본값에 임의로 약속된 추가 문자열을 추가하여 해시를 진행하여 기존 해시값과 전혀 다른 해시 값이 반환되어 알고리즘이 노출되더라도 원본 값을 보호할 수 있도록 하는 안전장치

3. 기존 : (암호화 하려는 값) =>  (hash값)

   Salt 사용 : (암호화 하려는 값 )+ (Salt용 값) => (hash값!)

### Crypto (NodeJs)

[Node Js내장 암호화 모듈!](https://nodejs.org/api/crypto.html)

````javascript
const crypto = require('crypto');

const secret = 'abcdefg';
const hash = crypto.createHmac('sha256', secret)//(알고리즘 방식, salt)
                   .update('I love cupcakes')// Hashing할 값
                   .digest('hex');// 인코딩 방식
console.log(hash);
// Prints:
//   c0fa1bc00531bd78ef38c628449c5102aeabd49b5dc3a2a516ea6ea959d6658e
````

 ## Cookie & Session & Token

### Cookie

서버가 사용자의 위치에 정보를 저장하고 불러올 수 있는 수단

1. 특정 호스트에서 생성된 쿠키는 이후 모든 요청마다 서버로 다시 전송
2. 이름, 값, 만료 날짜, 경로 정보로 구성

브라우저가 서버와 연결이 되었을 때 서버측에서 쿠키를 자동생성해서 해당 쿠키가 존재하지 않을경우 생성 후 response에 담아 보내줌(?)

```sequence
Client -> Server : Request
Server -> Client : Response (set cookie)\nkey1 = value1\nkey2 = value2
Client -> Server : Reqeuest (cookie)\nkey1 = value1\nkey2 = value2
```

쿠키를 지우기 전까지 데이터가 유지되면서 계속하여 server 에 같은 요청을 보냄

### Session

서버와 클라리언트의 연결이 활성화 된 상태

1. 서버가 Client에 대해 유일한 ID를 부여하여 서버 측에서 관리
2. 일반적으로 이 유일한 Client ID가 서버에서 존재하는 상황을 Session이라고 칭함
3. 각 Client ID의 Session객체마다 Data를 관리 할 수 있음
4. 사용자의 정보 중 보안상 중요한 데이터는 Session에서 관리함

### Token

인증을 위해 사용되는 암호화 된 문자열

1. Http 통신의 Stateless 특징과 알맞다
2. 유저의 인증 정보를 서버나 세션에 담아두지 않음
3. 유저의 활성화 여부를 신경쓰지 않고 넘겨진 요청에 담겨진 Token의 정합성만을 확인
4. 서버에서 클라이언트의 상태 정보를 저장하지 않고 클라이언트에서 넘겨지는 요청만으로 작업을 처리하게 되는데, 이런 경우 클라이언트 상태관리에 관한 비용이 없기때문에 서버의 확장성이 높음

```sequence
Client -> Server : Request Post/Login
Note right of Server : 세션 토큰 생성
Server -> Client : Response Post/Login\nset-cookie : \ntoken:session_token
Client -> Server : Request Get/info\ncookie : \n token:session_token
Note right of Server : 토큰 정보 검증
Server -> Client : Response Get/info\nset-cookei : \ntoken:session_token
```

## Shortly express sprint

- sequelize cli를 이용하여 db를 생성하고, 