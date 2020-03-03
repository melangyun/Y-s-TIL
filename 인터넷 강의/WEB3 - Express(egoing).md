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
`app.use`, `app.get`, `app.post` 등 으로 작성되었던 코드들은  대다수 **Application-level middleware**이다.

**미들웨어의 종류**

- Application-level middleware
- Router-level middleware
- Error-handleing middleware
- Build-in middleware
- Third-party middleware

### Application-level middeleware

````javascript
var app = express();

app.use(function(req, res, next){
    console.log('Time : ', Date.now())
    next()
})
````

app.use이후 function은 미들웨어로서 등록되게 된것이고, middleware의 핵심은 request와 response를 받아서 그것을 변형 할 수 있다. next라는 매개변수를 받아, 그것을 실행할지 혹은 실행 하지 않을지를 그 미들웨어의 이전 미들웨어가 결정하도록 한다.

다음 처럼 특정 경로에서만 사용하게 할 수 도 있다.(use대신 Post 나, get을 쓰면 post혹은 get으로 접근시에만 동작한다.)

````javascript
app.use('/user/:id',function(req, res, next){
    console.log('Request Type : ', req.method)
    next();
})
````

### 인자로 함수를 연속적으로 부여

인자로 함수를 연속적으로 주는 것을 통해서 인자를 여러개를 줄 수 있기도 하다.

````javascript
app.use('/user/:id',function(req, res, next){
    console.log('Request URL : ', req.originalUrl)
    next()
    //여기에서 next는 이 다음 호출 인자(funciton)을 가르킨다.
},function(req,rex,next){
    console.log('Request Type : ', req.method)
    next()
})
````

### next()가 없는경우

````javascript
app.get('/user/:id',function(req,res,next){
    console.log('ID : ', req.params.id)
    next()
},function(req, res, next){
    res.send('User Info')
	//next()가 없다.
})

//따라서 아래 코드는 실행되지 않는다. 
app.get('/user/:id',function(req,res,next){
    res.end(req.parmas.id)
})

````

### if문을 통한 라우트 실행

````javascript
app.get('/user/:id',function(req, res, next){
    if( req.params.id === '0 ') next('route')
    // 'route' 인자가 있는경우, 다음 라우터의 function이 실행된다.
    else next();//인자가 없는 경우 바로 다음 인자(function)이 실행된다.
}, function (req, rex, next){
    res.render('regular')
})

//인자가 있는경우 실행되는 라우트!
app.get('/user/:id', function(req, res, next){
    res.render('specail')
})
````

미들웨어를 잘 활용하면 application의 흐름을 자유자제로 제어할 수 있다.

## 12. 정적인 파일의 서비스

img, js, css 파일과 같은것들을 웹으로 다운로드 시켜주는것들을 정적인 파일이라고한다.

[Getting started_static files](https://expressjs.com/ko/starter/static-files.html) static이라고 하는 미들웨어가 내장하고 있는 파일을 미들웨어를 사용하면 된다!

````javascript
express.static(root, [options])
````

````javascript
app.use(express.static('public'))
````

**public directory**안에서 static files를 찾겠다!

````html
<!-- 이후 라고 입력하면 불러올 수 있음-->
<img src = "images/sample.jpeg"/>
````

## 13. 에러처리

### 404, Not Fount

가장 흔한 에러 - 404, not found - 검색 key : **express 404**

````javascript 
//가장 마지막에 표시!
app.use(function(req, res, next){
	res.status(404).send('Sorry cant find that!')
});
````

미들웨어를 추가한 것인데, 가장 마지막에 추가함.
미들웨어는 순차적으로 실행이되는데, 마지막까지 갔을 때 실행을 못했을 경우 찾지 못한 것 이므로, 404status를 보내주고 메세지를 보내는 작업을 수행하는것이다.

### 에러처리 - Error Handlers

[exrpess_Error handeler](https://expressjs.com/ko/guide/error-handling.html) 

````javascript
//앞서 처리한 404 코드 아래에 작성!
app.use(function(err, req, res, next){
    console.error(err.stack)
    res.status(500).send('Something broke!')
})
````

위로 올리면 안된다.
작성한 error handler의 경우 error을 넘기면 error handler의 미들웨어가 받게된다.

## 14. 라우터

sw가 커짐에 따라서 복잡도를 잘 정리정돈하지않으면 sw가 커지는데 한계가 있다.
[Guide Routing](https://expressjs.com/ko/guide/routing.html)참조!

````javascript
var express = require('express')
var router = express.Router();
//express가 갖고있는 Router()메소드를 호출함

router.use(function timeLog(req, res, next){
    console.log('Time : ', Date.now())
    next()
})

router.get('/', function(req, res){
    res.send('Birds home page')
})

router.get('/about', function(req,res){
    res.send('About birds')
})

module.exports = router;
//export중요!! -> 모듈로서 동작하기 위함
````

- 라우터를 파일로 분리시 분리된 파일 안에서 `/topic`까지 넣을 필요가 없음!

  ````javascript
  const topicRouter = require('./routes/topic');
  app.use('/topic' , topicRouter);
  
  // '/topic'으로 시작하는 주소들에게 topicRouter에 해당하는 미들웨어를 적용하겠다.
  ````

라우터의 기능을 이용하여 깔끔하게 정리정돈 할 수 있음!

## 15. 보안

Express참조문서의 [보안관련](https://expressjs.com/ko/advanced/best-practice-security.html) 문서

- Express의 회신버전을 항상 유지

- TLS(혹은 SSL) 사용
  (Http보단 Https를 쓰라는것! - 암호화 체결 유무!)

- Helmet 사용
  (자주 발생하는 보안문제를 자동으로 해결해주는 모듈!)
  `npm install --save Helmet`을 설치한 후

  ````javascript
  const helmet =  require('helmet');
  app.use(helmet());
  ````

  핼멧의 보안솔루션을 디테일하게 조정할 수 도 있음.(추가적인 공부 필요)

- 쿠키를 안전하게 사용
  방문자 한명 한명을 식별하는 매커니즘
  쿠키를 올바르고, 안전하게 사용해라!

- 인증 체계에 대한 브루스 포트 공격 방지

- 종속 항목이 안전한지 확인(**dependencies**)
  `npm install nsp -g` 보안을 확인해주는 모듈임!(글로벌 설치)

  `nsp check`를 체크

- 그 외의 알려져있는 취약점 회피 등

## 16. express generator

express를 이용해서 프로젝트를 진행할 때 초반은 거의 동일함.
express는 기본적인 구성에 해당하는 부분을 만들어주는 기능이 있다. [express generator](https://expressjs.com/ko/starter/generator.html) 문서에서 더 디테일한 내용 참조!

- 비어있는 directory에서 
  `npm install express-generator -g`
- `express myapp`이라고 하면 프로젝트가 자동으로 생성된다.
- 이후 안내대로 디렉토리를 바꾼뒤 `npm install`
- `pm2 start [directory]`혹은 `npm start`
- cf) jade라는 html 템플릿 엔진이 있음
- 템플릿 엔진 pug도 있음!(반복문, 조건문, clude, 상속 등 가능)
- 궁금하면 express안내서 [using-template-engines](https://expressjs.com/ko/guide/using-template-engines.html) 참조

### Express 는 미들웨어!!!가 가장중요하다.

**using third-party middelware**참조해보기