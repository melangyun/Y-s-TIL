

# Sokect.io를 사용한 실시간 채팅 애플리케이션

[poiemaweb](https://poiemaweb.com/nodejs-socketio)
HTTP는 무상태 프로토콜(stateless protocol)으로 어떠한 이전 요청과도 무관한 각각의 요청을 독립적인 트랜젝션으로 취급하는 통신 프로토콜이다. 이러한 HTTP의 한계에서 벗어나 Node.js에서 손쉽게 Real-time communication(RTC, 실시간 양방향 통신) 웹 애플리케이션을 작성할 수 있는 Sokcet.io를 간단한 채팅 애플리케이션 작성을 통해 알아본다.

## 1. WebSocket

WebSocket은 사용자의 브라우저와 서버 사이의 동적인 양방향 연결 채널을 구성하는 HTML5 프로토콜이다. WebSocket API를 통해 서버로 메시지를 보내고 요청 없이 응답을 받아오는 것이 가능하다.

HTTP는 클라이언트에 의해 초기화되기 때문에 서버가 변경사항을 클라이언트에게 알릴 수 있는 방법이 없지만 WebSocket의 연결은 HTTP 통신과는 다르게 클라이언트가 특정 주기를 가지고 Polling하지 않아도 변경된 사항을 시기 적절하게 전달할 수 있는 지속적이고 완전한 양방향 연결 스트림을 만들어주는 기술이다.

이러한 특성으로 인해 WebSocket은 서버의 데이터를 클라이언트에 즉시 전달 할 수 잇는 실시간 애플리케이션 작성에 매우 효과적인 프로토콜이다.

상세코드는 poeimaweb에서 확인!



## 2. Socket.io

HTML5 WebSocket은 매우 유용한 기술이지만, 오래된 브라우저의 경우 지원하지 않는 경우가 있다.
브라우저 간 호환이나 이전 버전 호환을 고려하여 Node.js를 위한 강력한 Cross-platform WebSocket API인 Socket.io를 사용하는 것이 바람직하다.

### install

````bash
$ mkdir socketio-chat && cd soetio-chat
$ npm install --yser
$ npm install --save --save-exact socket.io express
````

### Package.json의 내용은 다음과 같음

````json
{
  "name": "socketio-chat",
  "version": "1.0.0",
  "scripts": {
    "start": "node app"
  },
  "dependencies": {
    "express": "4.14.0",
    "socket.io": "1.4.8"
  }
}
````

## 3. Real-time Chat App

socket.io를 사용하여 클라이언트 간 Real-time Chat app을 구현하여 본다.

## 4.1 Server-side

````javascript
var app = require('express')();
var server = require('http').createServer(app);
// http server를 socket.io server로 upgrade한다
var io = require('socket.io')(server);

server.listen(3000, function() {
  console.log('Socket IO server listening on port 3000');
});
````

root url에 대한 라우트를 정의한다. localhost:3000으로 서버에 접속하면 클라이언트에 index.html을 전송한다.

````javascript
var app = require('express')();
var server = require('http').createServer(app);
var io = require('socket.io')(server);

// localhost:3000으로 서버에 접속하면 클라이언트로 index.html을 전송한다
app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

server.listen(3000, function() {
  console.log('Socket IO server listening on port 3000');
});
````

클라이언트가 socket.io서버에 접속했을 때 coneection이벤트가 발생한다. connection event handler를 정의한다.

````javascript
// connection이 수립되면 event handler function의 인자로 socket이 들어온다
io.on('connection', function(socket){
    
});
````

connection event handler function의 인자로 socket 객체가 전달된다. socket 객체는 개별 클라이언트와의 interacting을 위한 기본적인 객체이다. io 객체는 연결된 전체 클라이언트와의 interacting을 위한 객체이다.

connection event가 발생하면 (즉, 클라이언트가 접속하면) 클라이언트가 전송한 메시지를 수진하거나 클라이언트에게 메시지를송신한다.

**클라이언트가 전송한 메시지 수신**
**현재 접속되어 있는 클라이언트로부터의 메시지를 수신하기 위해서는 *on 메소드*를 사용한다.**


|Parameter|Description|
|------|---|
|event name|클라이언트가 메시지 송신 시 지정한 이벤트명(string)|
|function|이벤트 핸들러. 핸들러 함수의 인자로 클라이언트가 송신한 메시지가 전달된다.|


````javascript
socket.on('event_name',function(data){
    console.log('Meassage from Client : ' + data);
})
````

| Method                | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| io.emit               | 접속된 모든 클라이언트에게 메시지를 전송한다.                |
| socket.emeit          | 메시지를 전송한 클라이언트에게만 메시지를 전송한다.          |
| socket.broadcast.emit | 메시지를 전송한 클라이언트를 제외한 모든 클라이언트에게 메시지를 전송한다. |
| io.to(id).emit        | 특정 클라이언트에게만 메시지를 전송한다. Id는 socket 객체의 id 속성 값이다. |



| parameter  | Description                   |
| ---------- | ----------------------------- |
| event name | 이벤트명(string)              |
| msg        | 송신 메시지(strign or object) |



````javascript
// 접속된 모든 클라이언트에게 메시지를 전송한다
io.emit('event_name', msg);

// 메시지를 전송한 클라이언트에게만 메시지를 전송한다
socket.emit('event_name', msg);

// 메시지를 전송한 클라이언트를 제외한 모든 클라이언트에게 메시지를 전송한다
socket.broadcast.emit('event_name', msg);

// 특정 클라이언트에게만 메시지를 전송한다
io.to(id).emit('event_name', data);
````

#### 완성된 서버 측 코드

````javascript
var app = require('express')();
var server = require('http').createServer(app);
// http server를 socket.io server로 upgrade한다
var io = require('socket.io')(server);

// localhost:3000으로 서버에 접속하면 클라이언트로 index.html을 전송한다
app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

// connection event handler
// connection이 수립되면 event handler function의 인자로 socket인 들어온다
io.on('connection', function(socket) {

  // 접속한 클라이언트의 정보가 수신되면
  socket.on('login', function(data) {
    console.log('Client logged-in:\n name:' + data.name + '\n userid: ' + data.userid);

    // socket에 클라이언트 정보를 저장한다
    socket.name = data.name;
    socket.userid = data.userid;

    // 접속된 모든 클라이언트에게 메시지를 전송한다
    io.emit('login', data.name );
  });

  // 클라이언트로부터의 메시지가 수신되면
  socket.on('chat', function(data) {
    console.log('Message from %s: %s', socket.name, data.msg);

    var msg = {
      from: {
        name: socket.name,
        userid: socket.userid
      },
      msg: data.msg
    };

    // 메시지를 전송한 클라이언트를 제외한 모든 클라이언트에게 메시지를 전송한다
    socket.broadcast.emit('chat', msg);

    // 메시지를 전송한 클라이언트에게만 메시지를 전송한다
    // socket.emit('s2c chat', msg);

    // 접속된 모든 클라이언트에게 메시지를 전송한다
    // io.emit('s2c chat', msg);

    // 특정 클라이언트에게만 메시지를 전송한다
    // io.to(id).emit('s2c chat', data);
  });

  // force client disconnect from server
  socket.on('forceDisconnect', function() {
    socket.disconnect();
  })

  socket.on('disconnect', function() {
    console.log('user disconnected: ' + socket.name);
  });
});

server.listen(3000, function() {
  console.log('Socket IO server listening on port 3000');
});
````

## 4.2 Client-side

루트 디렉터리에 index.html을 생성한다.

클라이언트 라이브러리는 script tag의 src 어트리뷰트 값으로 "/socket.io/socket.io.js"을 지정하면 된다.
실제 path에 socket.io,js파일을 배치할 필요는 없다. 그 이유는 socket.io가 서버 기동 시에 socket.io.js라이브러리를 자동 생성해 주기 때문이다.

````html
<script src="/socket.io/socket.io.js"></script>
````

socket.io 서버에 접속하기 위해 io()메소드를 호출한다.

````javascript
var socket = io();
````

이때 생성된 socket으로 서버로의 메시지 송신 도는 서버로부터의 메시지 수신을 할 수있다.

**서버로의 메시지 송신**
현재 접속되어 있는 서버로 메시지를 송신하기 위해서는 emit메소드를 사용한다.

| Parameter  | Description                   |
| ---------- | ----------------------------- |
| event name | 이벤트 명(string)             |
| msg        | 송신 메시지(string or object) |

````javascript
socket.emit("evnet_name", msg);
````

**서버로부터의 메시지 수신**
현재 접속되어 있는 서버로부터의 메시지를 수신하기 위해서는 on 메소드를 사용한다.

| Parameter  | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| event name | 서버가 메시지 송신 시 지정한 이벤트 명(string)               |
| function   | 이벤트 핸들러. 핸들러 함수의 인자에 서버가 송신한 메시지가 전달된다. |

````javascript
socket.on("event_name", function(data) {
  console.log('Message from Server: ' + data);
});
````

**클라이언트 측 코드는 아래와 같음**

````html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Socket.io Chat Example</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
</head>
<body>
  <div class="container">
    <h3>Socket.io Chat Example</h3>
    <form class="form-inline">
      <div class="form-group">
        <label for="msgForm">Message: </label>
        <input type="text" class="form-control" id="msgForm">
      </div>
      <button type="submit" class="btn btn-primary">Send</button>
    </form>
    <div id="chatLogs"></div>
  </div>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
  <script src="/socket.io/socket.io.js"></script>
  <script>
  $(function(){
    // socket.io 서버에 접속한다
    var socket = io();

    // 서버로 자신의 정보를 전송한다.
    socket.emit("login", {
      // name: "ungmo2",
      name: makeRandomName(),
      userid: "ungmo2@gmail.com"
    });

    // 서버로부터의 메시지가 수신되면
    socket.on("login", function(data) {
      $("#chatLogs").append("<div><strong>" + data + "</strong> has joined</div>");
    });

    // 서버로부터의 메시지가 수신되면
    socket.on("chat", function(data) {
      $("#chatLogs").append("<div>" + data.msg + " : from <strong>" + data.from.name + "</strong></div>");
    });

    // Send 버튼이 클릭되면
    $("form").submit(function(e) {
      e.preventDefault();
      var $msgForm = $("#msgForm");

      // 서버로 메시지를 전송한다.
      socket.emit("chat", { msg: $msgForm.val() });
      $msgForm.val("");
    });

    function makeRandomName(){
      var name = "";
      var possible = "abcdefghijklmnopqrstuvwxyz";
      for( var i = 0; i < 3; i++ ) {
        name += possible.charAt(Math.floor(Math.random() * possible.length));
      }
      return name;
    }
  });
  </script>
</body>
</html>
````

