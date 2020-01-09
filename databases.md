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

- ㅋRuby on Rails (Ruby)
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

  ## 생활코딩 - mysql db생성부분만!
  
  ### mysql 접속
  
  ```mysql
  sudo mysql -uroot -p
  -- mysql -u[사용자] -p
  ```
  
  ### 스키마의 사용
  
  ```mysql
  CREATE DATABASE [이름];
  DROP DATABASE [이름];
  -- how to show DB list in my sql?
  -- 목록보기!
  SHOW {DATABASES | SCHEMAS} 
  [LIKE 'pattern'| WHERE expr]
  
  -- create 후 USE [db이름]으로 해줘야 사용 할 수 있다.
  USE [이름];
  ```
  
  



## ORM(Object-Relational Mapping)

- Sequelize
- Assiciation
- Transaction

### Sqeulize 사용하기1(sequelize init)

sqeqeulize는 nodeJs에서 웹을 DB에 연동할 때 raw Query문을 사용하지 않고 쉽게 다룰 수 있도록 도와주는 라이브러리 이다.
seqeulize는 DB에서 조회된 값을 객체로 전달해주는 ORM이다.
ORM이란 객체와 관걔형 DB의 관계를 매핑해주는 도구이다.

**sqeulize 다운로드 : **`npm install --save sequelize`
**mysql2 다운로드 : ** `npm install --sqve mysql2`
**sequelize-cli 전역으로 설치 : ** `npm install -g sequelize-cli` ??

````javascript
sequelize init
````

**config.json 파일생성됨 ** 

````json
//config.json은 DB 연동에 필요한 정보가 들어있다.
{
    "development" : {
        "username" : "root",
        "password" : "비밀번호",
        "database" : "db명",
        "host" : "localhost",
        "dialiect", "mysql",
        "operatorAliases" " false"
    }
}
````

### Sqeulize 사용2

`npm install sequelize`이후 파일작성

````javascript
var Sequelize = require('sequelize');
var db = new Sequelize('database_name', 'username', 'passord');

var User = db.define('User' , {
    username : Sequlize.STRING
});

var Message = db.define('Message', {
    userid : Sequelize.INTEGER,
    text : Sequelize.STRING,
    roomname : Sequelize.STRING
});

User.sync()
	.then(()=> User.create({ username : 'Jean Valjean' }))
	.then(()=> User.findAll({ where : {username : 'Jean Valjean'} }))
	.then((users) => {
    	users.forEach((user) => {console.log(user.username + 'exists')});
    	db.close();
	}).catch((err)=>{
    	console.log(err);
		db.close();
	})
````

## Sequelize CLI를 사용하여 User API만들기

[sequelize공식문서](https://sequelize.org/v5/)

![orm](https://images.velog.io/post-images/jeff0720/fc584920-f895-11e8-8150-b5d2c1881964/ORMMapping.png)

[참고블로그](https://velog.io/@jeff0720/Sequelize-CLI를-사용하여-간단한-User-API-만들기-vdjpb8nl0k)

ORM이란, **객체를 관계형 DB에 매핑해 DB의 기능들을 추상적으로 사용할 수 있게 해준다**는 개념이다.

예를들어, 관계형 DB만으로 기능을 개발한다고 했을 때, 테이블을 생성해주고 조회하고 업데이트, 삭제하는 쿼리를 작성해줘야한다. DB를 바꿔야 하는 상황이 생긴다면 해당 DB환경에 맞춰 쿼리를 다시 짜야하는 상황이 생길것이다.
ORM은 DB의 기능들을 추상화 했기 때문에, 어던 관계형DB이든 문제없이 기능을 사용할 수 있게 해준다.

### ORM을 사용하면 좋은점

- ORM을 통해 DB 쿼리를 추상화 해 본래 기능을 구현하는 로직에만 집중 할 수 있다.
- 특정 DB에 대한 종속성에 사라져, DB가 바뀌는 상황에서도 유연하게 대처할 수 이따.
- DB **마이그레이션**을 쉽게 할 수 있다.
  마이그레이션이란, 한 운영환경으로부터 다른 운영환경으로 옮기는 작업을 뜻한다.(ex. 윈도우 -> 리눅스)
  DB에서 데이터 마이그레이션이란, 데이터 베이스 스키마의 버전을 관리하기 위한 하나의 방법(데이터 전환)이다.
  개발 시스템에는 DB 스키마가 변경되었지만, 운영시스템의 데이터베이스 스키마가 변경되지 않았을 경우 마이그레이션을 수행산다.
  작게는 프로젝트 상 테이블 생성 및 변경작업부터 하나의 애플리케이션 또는 시스템을 옮기는 것 까지 마이그레이션이다.

### ORM을 사용의 단점

- Raw Query 를 사용하는 것 보다 성능이 떨어진다.

### Sequelize CLI는 무엇일까?

Sequelize CLI : The Sequelize command line interface : 명령어를 사용해 데이터베이스 작업을 할 수 있는 툴.
기능 : 마이그레이션, 시드, 모델

### Sequelize CLI사용

- `sudo yarn add sequelize mysql2`
- `./node_modules/.bin/sequelize`를 실행!(글로벌 설치시 일반 실행가능)
- `config` 파일을 통한 DB설정
- **Sequelize CLI모델 정의 및 마이그레이션**
  `마이그레이션`이란 `코드에 적혀져있는 DB테이블에 대해서 실제 DB에 테이블을 생성하는 개념` 
  예시 :  `node_moules/.bin.sequelize model:generate --name User pp attributes userId:string, name:string, engName:string`
  이라고 하면, 마이그레이션이 자동생성된다.
- **마이그레이션 작업**
  **마이그레이션 실행 : **`./node_modules/.bin/sequelize db:migrate` 명령어 작성 후 실행
  **마이그레이션 취소 : ** `./node_modules/.bin/sequelize db:migrate:undo`

### Sequelize CLI Seed를 사용해 데이터 추가하기

**Seed : 생성된 테이블에 데이터를 추가할 수 있게 해주는 기능**

- `./node_modules/.bin/sequelize seed:generage --name userData` : seeders 디렉터리에 userData파일 생성!
  up과 down이 있어서 up시에는 코드 실행, 취소시에는 down코드 실행!

### 이후 column추가 및 삭제기능, 폴더 이동기능도 있다.

따로 폴더 지정해주는 작업이 필요함. 블로그 참조하기!

## Sequelize Hooks

[참고 블로그](http://webframeworks.kr/tutorials/expressjs/expressjs_orm_four/) [목록](http://webframeworks.kr/tags/orm/) 추후 정독 필요함

Hooks는 insert, update, delete등의 작업을 수행하기 전이나, 수행한 후에 호출되는 기능을 뜻한다.
데이터베이스의 Trigger를 Sequelize에서는 Hooks라고 명칭한다. 데이터에 대한 변형이 이루어질대마다 작업해야하는 사항이 있을 때 hooks는 좋은 솔루션이 될 것이다.
Sequelize model의 메소드중 create, update, delete 와 validate작업 전후로 hooks(trigger)를 걸 수 있다.
hooks에 대한 메소드 종류는 다음과 같다.

1. create : beforeCreate, afgerCreate, beforeBulkCreate, afterBulkCreate
2. update : beforeUpdate, afterUpate, beforeBulkUpdate, afterBulkUpdate
3. destroy : beforeDestroy, afterDestroy, beforeBulkDestroy, afterBulkDestroy
4. validate : beforeValidate, afterValidate

### hooks를 추가하는 3가지 방법

#### 1. model define 시에 hooks에 대한 설정을 같이하는것

````javascript
module.exports = function( sequelize, DataTypes ){
    return sequelize.define('Publisher' , {
        pub_id: {type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true},
        name: {type: DataTypes.STRING(32), allowNull: false},
        established_date: {type: DataTypes.DATE, defaultValue: DataTypes.NOW}
    },{
       classMethods : {},
       tableName : true,
        underscored : true,
        timestams : false,
        hooks : {
            beforeCreate : function(){
                // create작업 전에 해야할 사항들
            }
        }
    });
}
````





