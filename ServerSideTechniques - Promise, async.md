# Sprint 3/3 Server Side Techniques



## Achevement Goals

1. 어떤 경우에 중첩된 callback이 발생하는지 이해한다.
2. Asynchronous code를 읽고 쓰기 편하도록 Promise를 사용해본다.
3. async/await keyword에 대해 이해하고, 작동 원리 및 장점 및 단점을 이해한다.
4. node fs moddule을 활용해 파일을 다룰 줄 안다.
5. HTTP server routing 을 다루면서 웹 서버가 어떻게 작동하는지 이해한다.

## Intro Server Side Techniques Sprint

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

- 비동기로 일어나는 작업들을 마치 순차적으로 일어나는것처럼 작업해주는것을 비동기처리!

### Objectives

1. 어떤 경우에 중첩된 callback이 발생하는지 이해한다.
2. 중첩된 callback의 단점을 이해한다.
3. Asynchronous code를 읽고 쓰기 편하도록 Promise를 사용해본다.
4. async / await keyword에 대해 이해하고, 작동 원리 및 장점, 단점을 이해한다.
5. Node.js의 fs모듈의 사용법을 이해한다.
6. node.js의 공식문서를 읽고 사용할 수 있다.

# 생활코딩 - fetch API 사용법

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

# Node.js에서 Request.js 사용하기

참고 블로그 링크 [Node.js에서 Request.js 사용하기](https://medium.com/harrythegreat/28744c52f68d?)

브라우저에서 자바스크립트를 쓴다면, fetch라는 내장 모듈이 있지만, 라이브러리 코드를 이용하면 훨씬 더 짧고 간결하게 코드릴 짤 수 있기때문에 라이브러리를 많이 사용한다.
**내장 모듈보다 무겁지만 인기있는 이유는 사용의 편의성때문이다.**

Node.js에서 가장 많이 사용되는 HTTP라이브러리는 단연 Request.js이다.

## Get 요청

### 1. 기본 형태

그냥 평문으로 작성하거나,  get 메서드를 통해 uri인자를 주면 된다.

```javascript
const request = require('request');

request('http://www.google.com',function(error, response, body){
   // callback 
});

request.get({uri:"http://www.google.com"}), function(error, response, body){
    //callback
})
```

### 2. Parameter가 있다면

```javascript
const options = {
	uri : "http://www.google.com",
    qs : {
        page : 5
    }
};
request.get(options, function(error, response, body){
    //callback
});
```

최종 url 는 `http://google.com?page=5`가 된다.

## Post 요청

### 1. Form 요청

```javascript
const options = {
    uri = 'http://google.com',
    method : 'POST',
    form : {
    key : 'value',
    key : 'value'
	}
}
request.post(options, function(error, response, body){
	//callback
});
```

post 메서드로 주는 첫번째 인자에 object에 보낼 form데이터를 작성한다.

### 2. JSON 요청

```javascript
let options = {
    uri: url,
    method: 'POST',
    body:{
      key:value
    },
    json:true //json으로 보낼경우 true로 해주어야 header값이 json으로 설정됩니다.
}
```

json옵션 설정이 필요하다.

**이후 form/Multipart data와 커스텀헤더, default설정 등 **블로그에 친절히 설명이 되어있으니 필요할때 참조하기!

## Promise 혹은 Await/Async와 함께 사용하기

`npm install --save request-promise-native`
`npm install --save request`
두 모듈 다 설치를 해야하지만, 사용할때에는 

```javascript
const request = require('request-promise-native')

const result = await request(options)
request(options).then().catch(err => callback(err));
```

하나만 사용해도 됨

# 자바스크립트 Promise 쉽게 이해하기

​	[링크](https://joshua1988.github.io/web-development/javascript/promise-for-beginners/)

## Promise

프로미스는 Js 비동기처리에 사용되는 객체이다.
프로미스는 주로 서버에서 받아온 데이터를 화면에 표시할 때 사용

## Promise의 3가지 상태

1. Pending(대기) : 비동기 처리 로직이 아직 완료되지 않은 상태
2. Fulfilled(이행) : 비동기 처리가 완료되어 프로미스가 결과 값을 반환해준 상태
3. Rejected(실패) : 비동기 처리가 실패하거나 오류가 발생한 상태

### 1. Pending(대기)

아래와같이 `new Promise()`로 메서드를 호출하기만 하면 **Pending(대기)**상태가 된다.

```javascript
new Promise();
```

이 때에 콜백 함수의 인자로 result, reject 에 접근 할 수 있다.

````javascript
new Promise(function(resolve, reject){
   //callback Function 
});
````

### 2. Fulfilled(이행)

콜백 함수의 인자 resolve를 실행하면 Fulfilled(이행)상태가 된다.

````javascript
new Promise(function(resolve, reject){
    resolve();
});
````

그리고, 이행상태가 되면 then()을 이용하여 처리 결과 값을 받을 수 있다.

```javascript
function getData(){
    return new Promise(function(resolve, reject){
       var data = 100;
        resolve(data);
    });
}

//resolve()의 결과 값 data를 resolvedData로 받음
getData().then(function(resolveData){
   console.log(resolveData);//100 
});
```

### 3. Rejected(실패)

reject인자로 reject()메서드를 실행하면 Rejected(실패)상태가 된다.

```javascript
new Promise((resolve,reject)=>{
    reject();
});
```

그리고 실패한 이유를 catch()로 받을 수 있다.

```javascript
function getData(){
    return new Promise(function(resolve, reject){
       reject(new Error("Request is failed")); 
    });
}

getData().then().catch((err)=>{console.log(err);})
//Error : Request is failed
```

## 여러개의 Promise 연결 - Promise Chaining

 ```javascript
new Promise((resolve, reject) => {
    setTimeout(function () =>{
               resolve(1);
	},2000);
})
.then((result)=>{
    return result+10; //11
})
.then((result)=>{
    return result+20;//31
})
 ```

## Promise 예시코드

```javascript
var userInfo = {
  id: 'test@abc.com',
  pw: '****'
};

function parseValue() {
  return new Promise({
    // ...
  });
}
function auth() {
  return new Promise({
    // ...
  });
}
function display() {
  return new Promise({
    // ...
  });
}
```

```javascript
getData(userInfo)
  .then(parseValue)
  .then(auth)
  .then(diaplay);
```

## Promise 에러처리

2가지 방법이 있다.

1. then()의 두 번째 인자로 에러를 처리하는 방법
2. catch()를 이용하는 방법 **더권장됨**

### 1. then()의 두번째 인자로 에러처리

````javascript
getData().then(
  handleSuccess,
  handleError
);
````

### 2. catch()를 이용하는 방법

```javascript
getData().then().catch();
```



# 자바스크립트 async와 await

[참조 블로그 링크](https://joshua1988.github.io/web-development/javascript/js-async-await/)

async와 await는 자바스크립트의 비동기 처리 패턴 중 최근에 나온 문법이다.
기존의 비동기 처리방식인 콜백함수와 프로미스의 단점을 보완하고 개발자가 읽기 좋은 코드를 작성할 수 있게 도와준다.

## async & await 적용 코드와 그렇지 않은 코드

```javascript
function logName() {
  var user = fetchUser('domain.com/users/1');
    //fetchUser를 HTTP 통신 코드라고 가정
  if (user.id === 1) {
    console.log(user.name);
  }
}
```

위 코드를 aasync 와 await를 추가해주면

```javascript
async function logName() {
  var user = await fetchUser('domain.com/users/1');
  if (user.id === 1) {
    console.log(user.name);
  }
}
```

이 코드는 비동기 콜백으로 보았을 때 아래 코드와 같다.

```javascript
function logName() {
  fetchUser('domain.com/users/1', function(user) {
    if (user.id === 1) {
      console.log(user.name);
    }
  });
}
```

## async & await 기본문법

```javascript
async function 함수명(){
    await 비동기_처리_메서드명();//HTTP통신을 하는 비동기 처리 메서드!
}
```

함수 앞에 async 라는 예약어를 붙이고, 함수 내부 로직 중 **HTTP통신을 하는 비동기 처리 코드** 앞에 `await`를 붙인다.
**비동기 처리 메서드가 꼭 프로미스 객체를 반환해야** `await`가 의도한 대로 동작한다.

# Discussion Async JS

 with 두현EES

- require과 Import의 차이?,
  import default~
- 반드시 알아야 할 개념
  1. Call-stack
  2. Web-API
  3. Event Loop
- 타이포라

# Sprint promises

## - Promise.all()

[mdn Pomise.all()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)

여러 프로미스의 결과를 집계할 때 유용하게 사용 할 수 있다.

Promise.all()메서드는 순회 가능한 객체에 주어진 모든 프로미스가 이행한 후, 혹은 프로미스가 주어지지않았을 때 이행하는 Promise를 반환한다.

- return
  - 매개변수로 주어진 순회 가능한 객체가 비어있으면 **이행한 Promise** (Fulfillled Promise)
  - 프로미스가 없으면, 비동기적으로 **이행하는 Promise**
  - 그렇지 않은경우 **대기중인 Promise**