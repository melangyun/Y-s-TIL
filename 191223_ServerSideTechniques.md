# Sprint 3/3 Server Side Techniques



## Achevement Goals

---

1. 어떤 경우에 중첩된 callback이 발생하는지 이해한다.
2. Asynchronous code를 읽고 쓰기 편하도록 Promise를 사용해본다.
3. async/await keyword에 대해 이해하고, 작동 원리 및 장점 및 단점을 이해한다.
4. node fs moddule을 활용해 파일을 다룰 줄 안다.
5. HTTP server routing 을 다루면서 웹 서버가 어떻게 작동하는지 이해한다.

## Intro Server Side Techniques Sprint

---

- Promises - Solo Sprint

- Article Collector - pair programming

  ### Objective : Learn Promises & async/await

  - callback pattern 은 Js의 비동기 작동원리를 잘 표현하는 패턴이지만, 중첩된 callback은 코드의 가독성을 떨어뜨리는 원인.
  - Promise는 비동기 함수의 표현을 보다 낫게 만듭니다. 그리고 ES7에 추가된 async/await keyword는 비동기 과정을 마치 순차적, 동기적 인 코드처럼 표현 할 수 있습니다.

  ### Objective : Learn Data Persistence

  - 데이터를 보존할 수 있는 여러 방법 중 파일 시스템을 이용한 방법을 살펴봅니다.

  ### Objective : Learn getting resources from web

  - node app을 만들면서 웹 페이지를 제공하는 것 이외에, 다른 종류의 작업들을 진행 할 수 있습니다.
  - 이번 시간에서는 데이터를 파일로 저장하는 것 이외에서도, 웹에서 resource를 가져오는 등 다양한 작업들을 알아볼 것입니다.

## Key Materials

---

1. Why Async
2. Callback
3. Promise
4. async await

- Event loop 다시 보고 정리하자.
- 비동기 처리 량이 많아질수록 작업 순서 추적이 어려워짐,
  Promise - resolve, reject -> resolve().then으로 이어나갈 수 있다.
- Promise Chaining : 잘못된 활용의 경우, Promise hell이 일어나므로 사용에 유의하자.
- async await : async함수라고 표기해주고, 기다리는 곳에서 await해줘야함.



## Sprint - Promises : 자바스크립트의 비동기 처리

---

- 비동기로 일어나는 작업들을 마치 순차적으로 일어나는것처럼 작업해주는것을 비동기처리!

### Objectives

1. 어떤 경우에 중첩된 callback이 발생하는지 이해한다.
2. 중첩된 callback의 단점을 이해한다.
3. Asynchronous code를 읽고 쓰기 편하도록 Promise를 사용해본다.
4. async / await keyword에 대해 이해하고, 작동 원리 및 장점, 단점을 이해한다.
5. Node.js의 fs모듈의 사용법을 이해한다.
6. node.js의 공식문서를 읽고 사용할 수 있다.

## 생활코딩 - fetch API 사용법

---

[강의링크1](https://www.youtube.com/watch?v=ufjCFdG_4fo&feature=youtu.be) [강의링크2](www.youtube.com/watch?v=qy3M0Cp0ios&list=PLuHgQVnccGMA9-1PvblBehoGg7Pu1lg6q&index=7) [강의링크3](https://www.youtube.com/watch?v=IKO8Dy_YsiY&list=PLuHgQVnccGMA9-1PvblBehoGg7Pu1lg6q&index=8)

ajax 를 구현하는 여러가지 방법 중 최신의 방법이 fetch API이다.

```javascript
fecth('css').then((res)=>{
    res.text().then((text)=>{
        alert(text);
    })
})
```

1. css파일이 불려옴
2. 모든 작업이 끝난 다음 then안의 내용을 실행.
3. 응답한 데이터가 text에 담겨있음을 숙지하자.

사용법은 생각보다 간단하다. 하지만 정확히 무엇을 return하고 받아오는 것인가 에 대한 물음 추가적으로 필요할 것이다.

1. fetch('javascript') : client 가 server에게, 브라우져야, js파일을 서버에게 응답해줘!
2. then() : 응답을 하는데에 시간이 오래걸릴 수 있다.
   'fetch'야, 응답이 끝나면 안의 callback함수를 실행시켜줘!

## Discussion Async JS

---

- require과 Import의 차이?,
  import default~
- 반드시 알아야 할 개념
  1. Call-stack
  2. Web-API
  3. Event Loop
- 타이포라



