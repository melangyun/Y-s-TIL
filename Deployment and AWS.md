# Deployment and AWS

AWS를 통해서 웹 서비스의 제작 및 구현 뿐만아니라 배포를 통한 고객에게 직접 서비스를 제공할 수 있다.

**스프린트 시작 전 알면 좋을 것**

1. 일반적인 블로그 서비스의 시스템 아키텍쳐를 간단하게나마 그릴 수 있다.
2. 새로운 OS에서 개발 환경을 다시 구축 할 수 있다.

**Precautions**

1. AWS services 는 프리티어로 이용하면 대부분 무료로 사용 할 수 있습니다.
   다만 AWS에서 요구하는 조건을 충족하지 않으면 소액 과금 될 수 있습니다.
2. Deployment라는 과정이 생소하고 어색할 수 있습니다. 당장에 모든 배포과정을 직접 설계 하지 않을 가능성이 높지만, 배포의 개념에 대해서 전혀 모르고 있다면 문제가 될 수 있습니다.

**Achievement Goals**

1. Deployment의 의미를 알고, 내 코드를 남에게 배포 할 수 있다.
2. 최소 AWS 서비스 블럭에서 3개 이상의 서비스를 활용하고, 설명할 수 있다.
3. ssh를 무엇을 위해 활용하고 알고, 다른 컴퓨터에 원격 접속 한다는 것의 의미를 설명 할 수 있다.
4. 보안을 위하여 github에 올리지 말아햐 할 코드를 gitignore로 따로 분류할 수있다.

# Intro Deployment

배포 : 내 코드를 다른 컴퓨터위에서 코드를 돌리고 그 서비스의 고객들이 코드를 실행시킬수 있는것.

## Running Code on Your Computer

로컬에서 직접 설정했기때문에 알수있었음

- Node version  : You know which one(s) are installed
- Dependencies : You know they're installed
- Port Number : You choose it
- Hostname : localhost or 127.0.0.1
- File Parhs : You know them
- API Keys : Present, but not checked into git

하지만 남의 컴퓨터에서는???? 모른다!!몰라!

**추천하는 방식 (Guarding against Assumptions)**

- Use root-relative URLs instead of absolute ones(절대주소 대신 상대주소로)

  ```html
  <a href="/signin">Sign In</a>
  ```

- Use enviroment variables to configure ports, et al

  ````javascript
  app.listen(process.env.PORT || 4568);
  ````

- install npm modules using --save
  `npm install --sqve express`, `npm install --save-dev grunt`

# Intro Deploy Strategy

베포해야 할 부분

1. SPA server strategy
2. Server Application deploy strategy

single page application : 사용자는 modules 의 수많은 파일을 다 받아야할까? 당연히 **No!**
리엑트는 *build*라는 파일이 있는데, 유저가 한번에 가져갈 수 있게 포장해준다(하나의 static한 파일로!).

그럼 이 파일을 어떻게 서브할까? **Build 파일 서브를 위한 cloud를 이용한다. : Amazon S3**
파일을 저장하는 cloud service!
S3를 사용하면 모바일 앱과 유사한 방식으로 다운로드 할 수 있음

- 혼자서 만들 때는 외부 접속을 고려 하지 않아도 되었다.
  하지만, 배포시에도 localhost:5000에 접속을 할 수 있을까?
  설정할 수는 있겠지만.. 외부인이 내 컴퓨터에 마구 들어오게 해서는 안된다.
  **EC2에 있는 Node app 에 접속해서 api를 받아간다!** 
  (다른 컴퓨터를 임차해서 해야함)

##  Amazon EC2

AWS가 가진 컴퓨터. 유저가 원격 접속 할 수 있다. (가상머신..) 
디비 구축을 위해서 클라우드 서비스를 이용한다. **AWS RDS !** 

 # Deploy Sprint Architecture

- Bare minmmum
  **S3**(react static serve) setup -> **EC2** (node server) -> **RDS**(mysql) 

- Advanced - https & Nightmare (4주 프로젝트때도 구축하기는 어려울것이나... 있다는것은 알아둘것)
  **https 웹사이트를 만드려면 어떻게 해야하는가? ** 프로젝트를 진행하면서 한번쯤 시도해 볼만 함
  ![Architecture](/home/yun/사진/DeploySprint Architecture.png)

  

# Sprint - S3

## React Build

- `npx create-react-app pratice-react-deploy` 리액트 앱 빌드
- 기본값인 `localhost:3000`이 아니라 **public link**로 build해야 함!
- create-react-app은 **build**라는 메소드를 제공한다 `yarn build`
  build는 js파일과 html파일, CSS파일 등을 **webpack**을 통해 하나로 합치어 하나의 정적 파일로 만들어주는 역할을 함

## Create Bucket

- 아마존 회원가입
- AWS Management Console에 들와 **S3**검색
- **버킷 만들기**클릭 후 생성
- 버킷에 들어와도 default설정으로 되어있기때문에 배포가 아직 불가능함.
- 버킷에 build create-react-app에서 만든 정적파일을 제공할 수 있도록 설정
  **정적 웹 사이트 호스팅** 
- 정적 웹사이트 호스팅 -> 이 버킷을 사용하여 웹사이트를 호스팅합니다.
  인덱스 문서, errorpage설정해주면 됨!
- 아직 버킷은 퍼블릭에서 접속할수 없는 private bucket이기 때문에 access deny메세지가 뜸!
  **권한 설정** 필요!

## Public Access

- 권한 탭
- 퍼블릭 엑세스 설정
- 새 퍼블릭 버킷 정책 차단, 버큿에 정책이 있는경우~ 해체
- 버킷정책 탭 : 아마존이 요구하는 template대로 작성해야하지만, 외우고있을수 있으므로 **정책생성기**를 통해 만들 수 있음 
  **상세 정책에 대한것은 문서 정독이 필요하다.**
- **Step1 : Select Policy Type - **Selct Type of Policy : S3 Bucket Policy
- **Step2 : Add Statement(s)**
- Effect : allow
- Principal : *
- AWS Service : Amazon S3
- Actions : GetObjcet
- ARN(Amazon Resource Name) : 특정한 형식을 가지고있고, 형식에 맞추어 등록해주어야함.
  이름 부분과 keyname설정..(문서 확인필요) 일단 모든파일의 경우는 *
- json타입의 정책이 생성됨 -> 정책생성에 맞추어 복사 붙여넣기
- 권한 설정이 되었지만 아직 404 페이지가 뜸 : 버킷에 static파일을 올리지 않았기때문에!
- 정적파일을 drag & drop을 하면 접속이 가능해진다!

# Sprint - EC2

## Create Server Application

(node server Application) 아마존에 배포!

- `mkdir pratice-node-server`
  `cd practice-node-server`
  `npm init`
  `yarn install express`

- Index.js 생성

  ````javascript
  const express = require('express');
  
  const app = exxress();
  
  app.use('/', (req, res) =>{
  	res.send('hello pratice node server deploy');    
  });
  
  app.listen(5000, ()=>{
     	console.log('server on 5000') 
  });
  ````

- cors문제를 겪에될것...

- git을 통해서 아마존의 EC2 서버 어플리케이션을 업로드 해주어야함!

## Start Instance

- EC2 탭에 들어옴

- 인스턴스 시작

- **단계1 : Amazon Machine Image(AMI)선택**

- Ubuntu Server 18.04 LTS 선택
  프리티어 사용 가능이라는 것을 확인하고 사용해야 과금당하지 않음

- 검토 - 읽어보고

- 시작하기

- 기존 키 페어 선택 또는 새 키 페어 생성 : **새 키페어 생성**
  키페어 이름 : pratice-server-deploy 
  키페어이름을 자시 다운도드 할 수 없으므로 반드시 키페어 다운로드 과정이 있어야 함!

- 인스턴스 시작

- 인스턴스 보기 : 이름 설정

- 연결클릭 & 인스턴스 엑세스 방법 읽고 따라하기

- 인스턴스에 연결 - 독립 실행형 SSH클라이언트

- 루트 폴더에 ssh가 있을것임.. 없으면 `mkdir`로 그냥 만들것

- 아까 받은 **키페어를 옮겨야함!** : `pratice-server-deploy.pem`

- 이후 `chmod 400 pratice-server-deploy.pem`

- `ssh -i  ~/.ssh/pratice-server-deploy.pem 54.180.8.42`

  54~는 IPv4 퍼블릭 IP
  이렇게 하면 우분투 컴퓨터로 접속한것!

- 우분투 컴퓨터는 Npm도, node 도 깔려있지 않으나, git은 설치되어있음
  github에 있는 파일을 클론하여 설치할수는 있으나, run time이 존재하지 않는 상태임

## Environment Settings

- 노드 설치 필요
  `sudo apt update`
  `sudo pat install nodejs`
  `sudo apt install npm`
  `nodejs -v` 정상 설치되었는지 확인!!!
- git clone 을 통해 다운로드(이전에 만든 서버!)
- depenency 만 npm install을 통해 설치함
- pulic IP를 통해 접속시 접속이 되지 않음 : *권한(보안설정)의 문제 때문!*

## Security Group

- EC2페이지에서 보안그룹 선택
- 기본적으로default name으로 부여된것이 있음
- SSH만 inbound로 부여가 되어있음
- 편집 클릭
- 규칙 추가
- 유형 : HTTP, 소스 위치무관
- 규칙추가
- 유형, 사용자지정 TCP , 소스 위치 무관
- 서버를 끄게되면 그냥 꺼져버림........ 어떻게 해서 계속해서 켜놓을 수 있을것인가??? PM2!

## Intro PM2

터미널을 종료해도 서버가 계속 켜져있을수 있도록 하는 proccess manager tool인 PM2에 대해서 알아봅시다.

`npm install pm2 -g`터미널을 꺼도 서버를 계속해서 동작하도록 하는 모듈.
`pm2 start index.js` 라고 하면 목록이 나옴
`pm2 list`동작 확인!

pm2를 통해 실행하고있으면 터미널을 꺼도 계속해서 동작하고있다.

# Sprint - RDS

 ## Create RDS Instance

- Cloud data service !!

- 협업을 하는데에 있어서 힘든 점은 각자의 컴퓨터의 상황이 다르기 때문에 안되는 경우 등등 다양한 문제가 발생할 수 있음....mysql상황이 다르다면 db접속부터가 문제인 경우가 다수이다.

- 따라서 db는 항상 cloud database를 권장함!

- RDS!!

- 데이터베이스 생성

- RDS 프리티어에 적용되는 옵션만 사용 체크! (mysql 설정)

- mysql 8번대 선택

- DB 인스턴스 식별자 : practice-database-deploy
  마스터 사용자 이름 : codestates
  마스터 암호 : ~
  다음단계

- **고급 설정 구성**

  퍼블릭 엑세스 가능성 : *예*로 설정

- 데이터베이스 옵션
  데이터베이스 이름 : mysql에 들어갈 db이름임
  port : 3306( mysql)기본포트 - 보안상의 이유로 변경 필요!!

- 생성!

## Connect RDS Database

