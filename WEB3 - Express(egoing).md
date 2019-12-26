# WEB3 - Express

## 1. 수업소개

Node js 의 등장으로 Js를 그대로 server쪽에서 사용 할 수 있게 되었지만, Node.js의 기능만을 가지고 직접 웹 애플리케이션을 구현하는 것은 다소 불편하다는 지적이 나오기시작했다.
이로인해 Node.js위에서 동작하는 Web Framework를 만들기 시작하였다.

### Web Framework?

반복적으로 어디에서 등장하는 일들을 처리할 때 더 적은 코드, 지식으로도 더 많은일을 보다 안전하게 처리 할 수 있도록 도와주는 도구.
프레임워크가 미리 구현해놓은 기능을 사용하고 웹 개발자는 웹의 개성에만 집중할수 있도록 만들어진 프로그램.

### Express

Node.js에서 동작하는 많은 프레임워크중에 가장 보편적으로 사용되는 프레임워크 중에 하나이다.
배우기 쉬운것과, 사용하기 편리하는것은 다르다. 더 적은 코드로 더 많은 일을 할 수 있다.

## 3. Hello Word

[express 공식문서](https://expressjs.com/ko/starter/hello-world.html)

아래는 공식문서에서 안내하는 기본 실행 코드이다.

````javascript
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))
````

- express도 결국에는 모듈이기 때문에 require이 필요하다.
- express를 함수처럼 실행시키고 있으며, return 값은 application으로 약속되어있다.

- **API reference**안내의 app.get사용법

  ````javascript
  app.get(path,callback[,callback...])
  //.get(경로, 경로로 들어왔을 때 호출될 코드!)
  ````

  get메소드는 보통 **route, routing**이라고 하는 역할을한다.
  routing 은 길을 따라 가다가 적당한 곳으로 응답을 해주는것!

  기존 node.js에서 라우팅은 아래 형식으로 구현된다.

  ````javascript
  if(pathname === '/'){
      //callback
  }
  ````

  express를 이용한것이 가독성이 좋고 깔끔하다!

- **app.listen**

  ````javascript
  app.listen(port, () => console.log(`Example app listening on port ${port}!`))
  ````

  application객체의 listen메소드의 첫번째 인자로 3000을 주면, listen이라는 메소드가 실행될때 비로소 web server가 실행되며, 3000번 포트를 리스닝하게되고, callback function이 실행되게 되는것이다. 
  기존 Node.js의 `app.js`와 동일하다!

## 5. 상세 페이지 구현

Express - Guide - Routing 에 대한 설명!

- **Route parameters** 
  `Route path : /users/:userId/books/:bookID`
  `Request UR: : http://localhost:3000/users/34/books/8989`
  `req.params : {"userId" : "34", "bookId" : "8989"}`

  ````javascript
  app.get('/users/:userId/books/:bookId',(req,res)=>{
      res.send(req.parmas)
  })
  ````

- app적용 예시

  ````javascript
  app.get('/page:pageId',(request, response)=>{
    response.send(request.params)
  });
  ````

  주소 창에 `http://localhost:3000/page/HTML`를 입력하면`{"pageId":"HTML"}`이 출력된다!

- **express redirect**

  ````javascript
  response.redirect(`/page/${title}`);
  ````

## 9. 미들웨어의 사용

익스프레스는 익스프레스의 주요기능을 두가지로 설명한다.

1. Route : 라우트
2. Middlewarea : 미들웨어

소프트웨어를 만들 때 다른사람이 만든 sw를 부품으로 하여 나의 sw를 만들어야 sw가 높아진다. 일단 이것을 middelware라고 생각하자.

**Express공식문서 -> Guide -> Third-party middle ware**
offical하지 않다면, third-party라고 한다.

### body-parser MiddleWare

- body-parser를 이용하면 훨씬 더 우아하게 post방식의 데이터를 받을 수 있다.
  body : 웹브라우져에서 요구한 데이터의 본체
  header : 데이터를 설명하는 헤더

  `npm install body-parser --save` 

- body-parser user Example

  ```javascript
  var express = require('express')
  var bodyParser = require('body-parser')
  
  var app = express();
  
  //form데이터는 이렇게 처리하면 됨!
  app.use(bodyParser.urlencoded({extended : false}))
  
  //json타입의 데이터는 이렇게 하면됨!
  app.use(bodyParser.json())
  
  app.use((req,res)=>{
     res.setHeader('Contnet-Type','text/plain')
     res.write('you posted:\n')
     res.end(JSON.stringfy(req.body,null,2))
  });
  ```

  ```javascript
  app.use(bodyParser.urlencoded({extended : false}))
  // bodyParser.urlencoded({extended : false})
  // 이 부분이 실행되면 return값으로 middleware가 실행된다.
  // 사용자가 전송한 Post데이터를 내부적으로 분석해서 모든 데이터를 가져온 다음에 callback을 호출하도록 약속되어있다.
  // 이후 request에 해당하는 인자에 body라는 property를 만들어준다.
  ```

  따라서 아래 코드를 body parser의 방식에 맞게 수정할 수 있다.

  ```javascript
  app.post('/delete_process', ( request, response ) => {
  	let body = '';
  	request.on('data', data => {
  		body += data;
  	});
  
      request.on('end', () =>{
          const post = qs.parse(body);
          const id = post.id;
          const filteredId = path.parse(id).base;
          fs.unlink(`data/${filteredId}`, (err)=>{
              response.redirect('/');
          });
      });
  });
  ```

  body parser를 사용한 후

  ```javascript
  app.post('/delete_process', ( request, response ) => {
      const post = request.body;
      const id = post.id;
      const filteredId = path.parse(id).base;
      fs.unlink(`data/${filteredId}`, (err)=>{
          response.redirect('/');
      });    
  });
  ```

### compression

web에 많은 사람들이 접속을하고, 데이터 사용량이 올라갈수록 시간과 돈의 소모가 많아진다. 이러한 문제를 압축을 통해 해결할 수 있다.

- 이 방식은 ~한 방식으로 압축해놓은것이니까, browser에서 알아서 풀어주세요!

라는 식으로 진행되면 데이터 사용량을 획기적으로 줄일 수 있다. 다만, 압축을 하고, 푸는 과정이 필요하지만, 네트워크의 전송비용 보단 싸고 빠르다.

**Google : express middelware compression**

``npm install compression``을 통해 설치

`const compression = require('compression')`을 통해 require

````javascript
const compression = require('compression');
const express = require('express');

const app = express();

app.use(compression());
//실행하면 middleware이 호출됨
````

강제리로드 `ctrl + shift + R` 을 통해 용량이 획기적으로 줄어드는 것을 확인 할 수 있다.

## 10. 미들웨어 만들기

`express`의 **Guide**에서 [미들웨어의 작성](https://expressjs.com/ko/guide/writing-middleware.html)을 볼 수 있다.

공통된 기능을 미들웨어로서 축약할 수 있다.

```javascript
app.use((request, response, next)=>{
  fs.readdir('./data',(error, filelist)=>{
      request.list = filelist;
      next();
	//3번재 인자의 function을 실행시킴(그다음 실행시킬 미들웨어가 담겨있음)
  });
});
```

이렇게 미들웨어를 작동시키고, get 이나 Post등 각각의 상황에 맞추어 request안의 속성으로 받을 수 있다. 하지만, use 는 get 과 Post 모두 응답하는 function을 이용하기 위함이며, 부분적으로 Post 요청시에는 필요하지 않을 수도 있다. 따라서 아래와 같은 코드 변화를 줄 수 도 있다.

````javascript
app.get('*',(request, response, next) => {
   fs.readdir('./data', (error, filelist) => {
       request.list = filelist;
       next();
   }) 
});
````

위와같이 작성시, post요청시 작동하지 않는다.

작성하다 보니, 기존 get방식과 Middelware의 형태가 매우 유사하다.

### express에서는 사실, 모든게 middleware라고 할 수 있다.

각각의 프로그램들이 서로가 서로를 연결해주는 작은 sw라는 점에서  middleware라고 하는게 아닐까?



## 11. 미들웨어의 실행순서

express 의 Guide의 [미들웨어의 사용](https://expressjs.com/ko/guide/using-middleware.html)을 기반으로 수업이 진행되었다.
미들웨어에는 여러가지 타입이 있다.
`app.use` 등 으로 작성되었던 코드들은  대다수 **Application-level middleware**이다.

### Application-level middeleware

`app.use`로 