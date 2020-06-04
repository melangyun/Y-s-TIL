# 생활코딩 WEB2 - Node.js

**📓️ 문서/exercise/생활코딩/web1_html_internet**

## 1. 수업 소개

- 사람이 직접 html을 타이핑하여 만들어야했다.
  -> 하나하나의 html구조를 바꾸려면 일일히 수정이 필요했고, 유저와의 상호작용도 힘들어짐, 성장의 한계에 봉착함.
- 이런 추세에 따라 이미 js에 익숙한 web개발자들이 새로운 컴퓨터 언어를 배우지 않고도 자동으로 서버쪽(server side Application) web을 만들고싶어하였다.
- nodeJs가등장하였고, 버전 업이 되면서, 웹 브라우저 뿐만아닌 컴퓨터 자체를 통제하기 시작하였다.

## 5. Node.js로 웹서버 만들기 

- [생활코딩 링크](https://opentutorials.org/module/3549/21032)

- Node.js 는 Apache와 같이 웹 서버로도 사용할 수 있다. 왜나하면 웹서버 기능을 내장하고 있기 때문이다.
  그러한 특성을 이용하면 Apache 웹서버로 할 수 없는 일을 할 수 있다! 예를들어

  ```javascript
  console.log( __dirname + url );
  //url에 무엇을 넣느냐에 따라서 경로를 달리 줄수 있다
  ```

  위와 같이 프로그래밍적으로 사용자에게 전송 내용을 바꾸는 것이다.

## 9. URL의 이해

- 다음 url을 예시로 볼 때  **http: opentutorials.org:3000/main?id=HTML?page=12**
  - **HTTP**는 통신규칙이다.
    웹 브라우저와 웹 서버가 데이터를 주고 받기 위해서 만든 통신규칙이다.
  - **opentutorials.org** 는 host(domain) **호스트, 도메인**이다.
    인터넷에 연결되어있는 컴퓨터를 나타내는 주소인 것이다.
  - **3000**은 **포트번호**이다.
    한대의 컴퓨터 안에 여러대의 서버가 있을 수 있다.
    클라이언트가 어느 서버로 접속할지 안내하는 번호와 같다고 이해하자.
    (cf : 설정하지 않았을 때기본은 80번 이다.)
  - **/main**은 **path**이다. 어떤 경로의 파일인가?
  - **?id=HTML?page=12** 는 **쿼리스트링**이다.
    쿼리스트링의 값을 변경하면 웹서버에게 데이터 전달이 가능하다.
    또한, 쿼리스트링의 시작은 ?로 하기로 약속되어있다.

## 12. Node.js의 파일 읽기 기능

#### CRUD(Create, Read, Update, Delete)

네가지 처리가 정보를 다루는 핵심적인 처리방법이다.
file을 어떻게 하면 node.js로 읽고, 생성하고, 수정하고 삭제할 수 있을것인가?

**Google : nodeJs file read** : nodeJs 공식홈페이지 -> fs.readFile

````javascript
fs.readFile('sample.txt','utf-8',(err,data)=>{
   console.log(data); 
});
````

## 18. NodeJs콘솔에서의 입력값

**syntax/conditaional.js**

- **I/O**(Input, Output)

  - Input - parameter : 입력되는 정보의 형식
  - Input - Argument : 실제로 받은 값

  input과 output에는 여러가지 종류가 있다. console 에서 입력값을 주려면 어떻게 해야할까?

  - **Google : nodejs console input parameters**
    `process.argv`명령어를 통해 node 실행시 node정보, 파일정보, console입력값을 받을 수 있다.
    입력 값을 활용하여 더 확장적인 console 활용과 프로그래밍이 가능하다.

## 19. App제작 - Not found, 홈페이지 구현

```javascript
const pathName = url.parse(_url, true).pathname;
```

- pathName을 이용하여 404를 구현하였고, path가 root('/')를 벗어나면 `response.end(404)`로 구현하였다.
- `fs.readFile`은 `queryData`를 통해 불러오는데, 이 파일이 `undefined`라면 홈페이지(따로 구현되어있지 않음)이므로, 제목영역`title`과 설명`description`을 따로 할당해주는 형식으로 홈페이지를 구현함

## 23. Node.js에서 파일목록 알아내기

**google : nodejs file list in directory**

```javascript
//fs.readdir
const testFolder = './tests/';
const fs = require('fs');

//read dir
fs.readdir(testFolder, (err, files)=>{
    files.forEach( file =>{
       console.log(file); 
    });
})
```

**📓️nodejs/readdir.js**

## 24. App 제작 - 글목록 출력하기

앞서 수업에서 학습했던 fs.readdir를 통해 파일 목록을 받아와, a태그와 파일 리스트를 template literal을 통해 html태그로 출력함!

## 26. App 제작 - 함수를 이용해서 정리정돈하기

기능단위로 function을 분리하여 코드 중복을 줄이고 심플하게 만듬!

## 28.Nodejs에서 동기와 비동기(Synchronous & asychronous)

- 동기적인 방식 : 한가지 일을 끝날때 까지 기다렸다가 처리
  비동기적 방식 : 병렬적으로 진행! - 효율적이지만, 매우 복잡함!

- Node.js 공식문서에서의 예시

  - `fs.readFile(path[,options], callback)`
  - `fs.readFileSync(path[,options])`

  동기 방식의 경우 callback함수가 없는것에 유의하자. 또한, 기본적인 옵션이 비동기인것을 보아 node자체가 비동기적인 방식을 더 선호하는 것을 알 수 있다.

- 📓️syntax/sync.js
  파일 경로는 현재 파일이 아니라, node의 실행 위치에 따라 갈린다.

- 동기적인 방식

  ```javascript
  const fs = require('fs');
  
  console.log('A');
  const result = fs.readFileSync('syntax/sample.txt', 'utf-8');
  console.log(result);
  console.log('C')
  ```

  실행결과는 `ABC`

- 비동기적인 방식
  **동기적 방식은 return값이 있지만, 비동기적인 방식은 return값이 없다.**

  ```javascript
  const fs = require('fs');
  
  console.log('A');
  fs.readFile('syntax/sample.txt', 'utf-8', (err, result)=>{
     console.log(result); 
  });
  console.log('C');
  ```

  결과는 `ACB`

- **Callback : 앞서 작업 후 추우에 실행하라는 함수** 라고 생각하자.
   📓️syntax/callback.js

## 29. Node.js의 패키지 매니저와 PM2

### Package Manager

- sw들을 설치, 관리, 업데이트, 삭제해주는 프로그램이다.
  - NPM : nodeJs에서 가장 광범위하게 사용하고 있는 패키지 매니저이다.
  -  PM2 : production process manager for Node.js
    PM2를 이용하면 실행중인 프로그램(node js로 만든 프로그램 - main.js)을 꺼지면 다시켜준다.
    pm2가 파일이 수정이 되는지 관찰하고 있다가 파일을 수정하면 껐다가 다시 켜주기도한다. 
    Nodemone같은 친구인것 같다. 사용법 및 명령어는 `메모.md`와 구글링 참조

## 32. App제작 - POST방식으로 전송된 데이터 받기

- post qkdtlrdmfh 사용자가 전송한 값을 어떻게 받을것인가?
  **Google : nodeJs post data**

  ```javascript
  const qs = require('querystring');
  
  function(request, response){
      if(request.method === 'POST'){
          let body = '';
           /*
           웹 브러우저가 Post 방식으로 데이터를 전송 할 때 
           데이터가 엄청나게 많으면 데이터를 한번에 처리할 때 무리가 있을 수 있다.
           따라서 nodeJs에서는 post 전송방식의 데이터가 많을 것을 대비하여 아래의 사용방법을 제공하고있다.
           조각조각의 데이터들을 서버에서 수신할 때 마다 콜백함수를 호출하도록 약속되어있다.
           또한, data라는 인자를 통하여 수신하도록 약속되어있다.
         */
          request.on('data',(data)=>{
              body += data;
              if(body.length > 1e6) request.connection.destroy();
              /*
              이렇게 전송된 데이터가 너무 크다면 요청을 끊어버리는 코드이다.
              일종의 보안장치이며 없어도 무방하다.
              */
          });
          
          request.on('end',() =>{
              const post = qs.parse(body);
              /*
              모듈의 함수 중 parse라는 함수에다가 
              지금까지 저장한 body를 입력값으로 주면 post 정보를 준다!
              */
              const title = post.title;
              //설정한 InputTag의 name속성으로 들어온다.
          });
      }
  }
  ```



## 33. App제작 - 파일 생성과 리다이렉션

- 파일생성 : **Google : fs.writeFile**
  **fs.writeFile(file, data[,options],callback)** - options는 utf8을 주면된다!

  ```javascript
  const fs = require('fs');
  
  fs.writeFile('message.txt','Hello Node js',(error)=>{
      if(err) throw err;
      console.log('The file has been saved!');
  })
  ```

- 리다이렉션

  ```javascript
  response.writeHead(302,{Location : `/?id=${title}`});
  response.end()
  ```

  cf ) 302는 페이지 리다에렉션 코드이다.

## 36. App제작 - 파일명 변경, 내용 저장

- **Google : nodeJS file rename**

  ```javascript
  const fs = require('fs');
  
  fs.rename(oldPath, newPath, callback);
  ```

## 37. App제작 - 글삭제

- 삭제의 경우 절대 get방식으로 구현되어서는 안된다.
  form태그로 만들어 id를 submit 해주면 title을 id로 받아 삭제하는 기능을 만들것이다.
  이 경우 form태그의 Onsubmit기능을 이용해 js코드를 삽입할 수 있으므로 추후 다시한번 확인하는 기능을 넣을 수 도 있을것이다.

- 파일 삭제
  **Google : nodejs delete file**

  ````javascript
  const fs = require('fs');
  
  fs.unlink('path/file.txt',(err)=>{
      if(err) throw err;
      console.log('path/file.txt was delete');
  });
  ````

## 43. App제작 - 템플릿 기능 정리정돈하기

- 만들뒀던 function들을 object를 통해 정리함!
- 리펙토링의 필요성 : 일단 짜고, 추후에 고치는것 부터 시작하자.
  시작부터 완벽할순 없다.

## 44. Node.js 모듈의 형식

**📓️node.js/muse.js**, **📓️node.js/mpart.js**

````javascript
module.exports = M;
````

module이라고 하는 약속된 객체를 통해 M이 가르키는 것을 파일 밖에서 사용 할 수 있게 해주겠다는 약속이다.
모듈을 가져올 때는 require이 필요하다.

## 46. App제작 - 입력정보에 대한 보안

- **Goole: noejs path parse**

  ````javascript
  path.parse('/home/user/dir/file.txt');
  
  //이를 받아 콘솔을 찍어보면
  /*
      Return : {
      root: '/',
      dir:'/home/user/dir',
      base:'file.txt',
      ext :'.txt',
      name:'file'
      }
  */
  ````

  `base`는 최하위 경로만 받아온다.
  따라서 **base**사용시 경로 세탁이 가능할 것이다.

- 사용자에게서 들어오는 경로 정보와 출력되는 경로 정보는 모두 의심할 필요가 있다.

  ````javascript
  const path = require('path');
  const filteredId = path.parse(queryData.id).base;
  //경로정보에 모두 filteredId를 넣어야한다.
  ````

  

## 47. App제작 - 출력정보에 대한 보안

- XSS : Cross Site Scripting -> script태그를 삽입함으로서 일어 날 수 있는 보안문제이다.
  해결방법

  1. 직접 열어서 script를 지워버림
  2. 꺽쇄를 웹브라우저에 표시함! -> `HTML entyties`
     이 경우 이미 만들어진 모듈을 사용하여 간편하게 이용할 수 있음!
     **npm sanitize html**

- npm init : 프로젝트를 npm으로 관리하기 위한 시작
  아무 모듈을 쓰는 것은 비추천하며 평판을 보고 이용하길 추천함.

- `npm install -S sanitize-html`

- 설치 이후 dependencies목록에 등록된다.
  이것을 설치하면 이 프로젝트가 sanitize-html에 의존한다는 의미이다.
  한가지 모듈을 설치해도 여러개가 생기는 이유는, 설치한 모듈이 의존하고 있는 여러가지 모듈들이 함께 설치되기 때문이다.

- 모듈의 사용법은 **모듈 안내서**에 잘 적혀있다.

  ````javascript
  var sanitizeHtml = require('sanitize-html');
  var clean = sanitizeHtml(dirty);
  ````

  파일을 불러오는 곳에서만 사용하면 된다.
  잘 적용하면 스크립트 태그는 불러오지 않으며, 일반적인 html태그는 태그만 없에고 내용은 살려준다.
  더 디테일 한 설정을 보기 위해서는 모듈 설명서를 정독하면 알 수 있다.(쉽다고는 하지 않음)

## 48. API와 Create Server

### API : Application Programming Interface

- nodeJs의 버전 설명서에 들어가면 node모듈들의 설명 및 기능들이 나온다.
- 일단 createServer 만 간단히 정리하고 넘어갈것이다.
- `http.createServer([requestListener])` 대괄호는 생략 가능하다.
  requestListener는 `function`이며, **외부에서 요청이 들어올 때 마다 인자의 함수를 실행시킨다**는 것이다.
  첫번째 인자는 `request`, 두번째 인자는 `response`이다.
- `createServer`는 return값으로 http.server를 반환한다.
  http.server 는???
  app.listen-> server.listen()
  Start the HTTP server listening for conections
  This methods is identical to server.listen() from net.Server

## 49. 부록 - pm2 보충학습