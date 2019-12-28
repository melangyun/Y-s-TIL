# Databases

## Schema & Query Design slide

### What are we trying to do?

- 데이터 사이의 관계를 알아본다.
- 관계를 표현하는 방법?
- 어떻게 데이터 베이스를 효과적으로 짤 수 있는가?
- 관계로 묶여있는 데이터들을 어떻게 query문으로 가져올 수 있을 것인가?

**새로운 서비스를 만들 때 필요한것? **
화면을 먼저 짜보고, **어떤 데이터가 필요한가?**를 생각해보는것이 좋다.

### what is a schema?

**DB의 청사진**이다.
A schema is a description of the way data is organized in a database and the relationships among its diffenrent entities.
You can think of it as a "blueprint for your database".



### Entity와 Field

![Entity](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkav9T9eJYhdohHuWf9ZvG7sYxfA1vQz_1kMcZXrReBNGP86ri&s)

관계형 DB는 테이블 사이의 **관계**를 나타내는 것이다.

### mysql

```mysql
show tables;
-- 지금 가지고 있는 모든 테이블을 보여줌
describe classes;
-- class속성을 나타내줌
```

## MVC design pattern

![mvc패턴](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/327/1262.png)

![mvc패턴](https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Router-MVC-DB.svg/1200px-Router-MVC-DB.svg.png)

### what is MVC

Model View Controller : 일련의 sw가 돌아가는것에 대한 하나의 디자인, 패턴
코드 가독성, 관리성이 높아짐

### MVC패턴을 사용하는 프레임워크들

- Ruby on Rails (Ruby)
- Laravel(PHP)
- Codeigniter(PHP)
- Django(python)
- Flash(python)
- Express(JS)
- Backbone(JS)
- Angular(JS)

### 1. Model

DB와 연결이 되어있음

- knowledge
- handles data
- Interaction with DB

### 2. VIew

- visual representatin of a model
- what the users see(UI)

컨트롤러와만 이야기함!

### 3. Controller

- receives input
- process requests
- get data from a model
- pass data to the view

액션과 이벤트의 값을 받고, model에게 가공된 데이터를 넘겨줌.또한 Model로 부터 받은 데이터를 여러 가공을 거쳐 View에게 돌려줌

### MVC pseudo code

````javascript
//http://yourapp.com/users/profile/1

//routes
//users/profile/:id = Users.getProfile(id)

//controllers
class Users{
    function getProfile(id){
        profile = this.UserModel.getProfile(id)
        renderView('users/profile',profile)
    }
}

//models
class UsersModel{
 	function getProfile(id){
        data = this.db.get('SELET * FROM users WHERE id = id')
        return data;
    }   
}

//views
//users/profiled
/*
<h1>{{profile.name}}</h1>
<ul>
	<li>Email : {{profile.email}}</li>
	<li>Email : {{profile.phone}}</li>
</ul>
*/
````



## Intro Database & SQL

- SQL이 어떻게 이루어져 있는지 이해한다.
- SQL기본 query문을 사용할 줄 안다.
- Schema의 설계방법과 나은 방향성을 고안한다.
- 서버와 클라이언트 사이에서 주고 받는 데이터를 DB에 저장하여 영속성 있게 저장 할 수 있다.

### SQL이란?

Structed Query Language : 구조화된 Query언어
데이터 베이스 용 프로그래밍 언어!

데이터베이스에 query를 보내 원하는 데이터만을 뽑아 올 수 있다!

**Query란?**

- 직역하면 '질의문'
- 검색창에 적는 검색어도 Query의 일종
- 저장되어 있는 정보를 필터하기 위한 질문

### DB

- In-memory : 끄면 데이터가 없어짐
- File I/O : 원하는 데이터만 가져울 수 없고 항상 모든 데이터를 가져온 뒤 서버에서 필터링 필요
- Database : 필터링 외에도 File I/O로 구현이 힘든 관리를 위한 여러 기능들을 가지고 있는 데이터에 특화된 서버

## SQL Exercise

헷갈린 문제

- Select all records where the first letter of the `City` is an "a" or a "c" or an "s".

  ```mysql
  SELECT * FROM Customers
  WHERE City LIKE '[acs]%';
  ```

- Select all records where the first letter of the `City` starts with anything from an "a" to an "f".

  ```mysql
  SELECT * FROM Customers
  WHERE City LIKE '[a-f]%';
  ```

- Select all records where the first letter of the `City` is NOT an "a" or a "c" or an "f".

  ```mysql
  SELECT * FROM Customers
  WHERE City LIKE '[^acf]%';
  ```

  



