# 서버와의 통신

## Browser 

컴퓨터는 2진수만 알아듣는다.
그럼에도 불구하고, HTML, CSS, JS등으로 작성한 코드를 컴퓨터에서 볼 수 있는 이유는 바로 브라우저 덕분이다.!

[D2_브라우저는 어떻게 동작하는가?](https://d2.naver.com/helloworld/59361)

## Server

자원을 serve하는 주체, 리소스 요청과 응답에 대한 처리
클라이언트가 커피 원두를 음료로 먹으려면 어떻게 해야할까? : 바로 서버가 필요하다!

## API : Application Programming Interface

프로그래밍 되어있는 애플리케이션과 의사소통 가능한 매개체

서버 자원을 잘 가져다 쓸 수 있게 만들어놓은 인터페이스, 한마디로 메뉴판이다.
메뉴판이 있어야 서버는 원두를 바탕으로 음료를 만들어 제공 할 수 있다.
서버도 메뉴판이 필요하다. 그래야 클라이언트가 리소스 요청 및 생성을 할 수 있다.

- get : 메세지 전달로 주로 쓰임
- post : 메세지 저장으로 주로 쓰임

## HTTP : HyperText Transfer Protocol

프로토콜 : 규약, 규칙;
클라이언트와 서버가 통신하기 위해서 규약과 규칙을 지켜야한다.

클라이언트와 서버가 통신할 때 http규칙에 의해 클라이언트와 서버가 통신한다.
(TCP/IP중 가장 상위 규약이다.)
**작동방식**은 **항상** 요청과 응답으로 이루어진다! (없으면, 없다고 반드시 응답)

구성 : 응답과 요청 모두 헤더(header)와 바디(body)를 가짐

- header
  - origin : 어디에서 보내는 요청인가
  - content - type : 컨텐츠 타입은 무엇인가
  - user - agent : 어떤 클라이언트를 이용해 보냈는가
- body : 각 method가 body를 가지는지 mdn 에서 확인
  - [mdm_영문](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
  - [알아둬야 할 HTTP 공통 & 요청 헤더](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

속성

- stateless : http의 각 요청은 모두 독립적이다. 따라서 state라는 것이 없다.
- ConnectionLess : 한번의 요청에는 한번의 응답을 한다.

methods - get/ post / put / delete

- get : 서버에 자원을 요청
- post : 서버에 자원을 생성
- put : 서버에 자원을 수정
- delete : 서버의 자원을 제거

## AJAX

- 이전방식 : form.html 의 서버  전송 및 처리 -> result.html 화면전환
  (깜빡임이 있음 : 전체 페이지 리렌더링으로 부담감이 큼)

- **Dynamic web page의 등장**
  서버와 자유롭게 통신 할 수 있고 (XMLHttpRequest XHR의 등장),
  페이지 깜빡임 없이 seamless하게 작동하는 (JM DOM이용) 단순한 web page가 아닌, 보다 애플리케이션 다운 web app의 등장

- fetch API => 보다 쓰기 쉬운 표준 API

  ```javascript
  fetch('http://52.78.213.9:3000/messages')//get 요청의 부분...
  .then(
  (res) => res.json();
  )
  .then(
      (json)=>{
  		//json형태로 전달받은 서버로부터의 응답
      }
  )
  ```

  post 요청은 어떻게 보낼까? -> MDN : using Fetch
  최신 기술이라고 fetch가 전부 좋은 것은 아니며, 여전히 XMLHttpReqeust는 많이 쓰는 기술이므로, fetch와 XML HttpRequest와 차이점을 확인 한 후 사용하는 것이 좋음

### Why we Use Fetch?

- fetch : '가져옴' -> 어떤 것을 가져오는 function이다.
  무엇을 가져오기위해 ? 서버 자원!
- 클라이언트 - fetch -> 서버 리소드 -> 클라이언트

### fetch만 가능할까?

1. xmlHttpRequest
2. jQuery ajax
3. fetch : 조금 더 강력하고 유연함. mdn공식문서를 읽어보자

## 보안문제

### XSS (Cross-site Scripting)

게시판이나 웹 메일 등에 자바스크립트와 같은 스크립트 코드를 삽입해 개발자가 고려하지 않은 기능이 작동하게 하는 보안공격
클라이언트가 서버를 신뢰하여 발생하는 보안문제이다.
서버에서 넘어오는 작업을 신뢰할 수 잇다고 생각한 후 랜더링하여 발생!

### CSRF(Cross-site Request Forgery) 사이트 간 요청 위조

웹 애플리케이션 취약점 중 하나로 사용자가 자신의 의자와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 한다거나, 수정, 삭제 등의 작업을 하게 만다는 공격방법.

이는 XSS와는 반대로 서버가 클라이언트를 신뢰해서 발생하는 이슈이다.
서버는 인증정보를 가져오면 믿는다. 사용자는 인증 정보를 가진 채로 해커의 링크를 누르면, 해커는 인증정보를 가로채서 서버에 요청을 보내버린다.

### XSS와 CSRF는 어떻게 막을 수 있을까? - CORS

브라우저에서 기본적인 XSS공격방법은 막혀있다.
**Bwser Security Moduel -> CORS(Cross-Origin Resource Sharing)** : 다른 origin간의 resource를 공유함.

처음 전송되는 리소스의 도메인과 다른 도메인 으로부터 리소스가 요청될 경우 해당 리소스는 cross-origin HTTP 요청에 의해 요청된다.
예를들어 http://domain-a.com으로부터 전송되는 HTML페이지가 <img> src 속성을 통해 http://domain-a.com/image.jpg를 요청하는 경우가 있다. 오늘날 많은 웹페이지 들은 CSS스타일 시트, 이미지, 그리고 스크립트와 같은 리소스들을 각각의 출처로 부터 읽어온다.