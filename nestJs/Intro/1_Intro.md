# Intro

## nestJs란?
> Nest (NestJS) is a framework for building efficient, scalable Node.js server-side applications.

nestJs란 효율적이고 확장가능한 node.js 기반 서버 프레임워크이다. <br>
typescript를 공식적으로 완전히 지원한다. (js파일로도 작성이 가능하지만, 기능 제약이 있다.)<br>
default HTTP server framework로 Express를 사용하고 있으며, fastify를 선택적으로 사용 가능하다. 따라서 이를 기반으로 하는 서드파티 모듈이 자유롭게 활용 가능하다.

### 철학
node.js덕분에 Javascript는 web 의 front-end 와 back-end 모두에서의 "lingua franca"가 되었다.<br>
<br>
![lingua franca](./image/lingua_franca.png "lingua franca")<br>
<br>
그 결과 Angular, React 및 Vue와 같은 프레임워크가 생겨 생산성 높은  프론트 애플리케이션을 만들 수 있었다. <br>

node.js는 보편적으로 유연한 프로젝트 구조 및 아키텍쳐를 사용할 수 있으며, 이에 따라 빠르게 서버를 띄우는 것이 가능하다.<br>
<br>하지만 이것이 장점이다 단점으로 작용한다.

> However, while plenty of superb libraries, helpers, and tools exist for Node (and server-side JavaScript), none of them effectively solve the main problem of - Architecture.

프로그램 아키텍쳐 및 파일 구조는 사실 정답이랄게 없다. 가장 유명하고 보편적인 Express의 경우 프로젝트를 어떻게 구성할것인가를 알려주지 않는다.

> 깊은 고민과 고찰(?) 없이 초심자의 마음으로 프로젝트를 시작하게 되었을 때 프로젝트 구조가 커질수록 인터페이스 문제로 점점 스파게티 코드가 되어가곤 헸다... 

![스파게티 코드](http://i.imgur.com/eoF7lEG.jpg "스빠게띠")

<br> 물론 [이 글(Bulletproof node.js project architecture )](https://softwareontheroad.com/ideal-nodejs-project-structure/)과 같이 튼튼한 아키텍쳐를 위한 지침을 지시해주는 글들이 꽤 많고 정말 좋다. 하지만 각각의 아키텍쳐 지침들을 이해하고 어디까지 구현할 것인지, 기존 코드들을 뜯어고치는 시간들이 내게 있어서 굉장히 고되고 고민되었다..<br>
이러한 고민과 공부의 시간들을 단축시켜주는것이 바로 nestJs라고 생각한다.

> nest provides an out-of-the-box application architecture which allows developers and teams to create highly testable, scalable, loosely coupled, and easily maintainable applications. The architecture is heavily inspired by Angular.

nestJs는 (거의)정형화된 인터페이스를 제공해주며, 논리적이며 효과적인 파일 트리를 구성하기 쉽고, 코드의 유지 보수가 쉽다.<br>
> 개인적으로 Spring과 구조가 매우 유사하다고 느꼈고, 그래서 첫 학습 때에 러닝커브가 조금은 낮지 않았을까 생각한다.<br>하지만, Spring과 비교 할 수 없이 초기 세팅이 간단하다

정형화된 인터페이스를 사용한 다는 것은, 다른 말로 할때에 협업이 비교적 수월해 지고 코드 가독성이 좋아진다는 것이기도 하다고 생각한다.
<br>

### 세팅
Spring에 비할 바 없이 세팅이 간단하지만, Express에 비하면 복잡해 진다. 하지만, 미친듯이 친절한[공식문서](https://docs.nestjs.com)가 있고, 공식으로 서포트 하는 [디스코드](https://discord.gg/HhXdZKG)가 있어 세팅을 하거나 코딩을 할때 막히거나 에러가 있다면 질의응답이 가능하다.
<br>
(물론, 자주 부닫히는 질문들은 일단 찾아보면 왠만히 나오기도 한다 하하)

# 시작하기
표준(standard)아키텍쳐(monolithic)로의 시작은 정말 간단하다.<br>
1. nest cli를 설치하고, 
2. cli로 프로젝트를 만들면, 

당장 서버를 켜야할 때 필요한 모든게 세팅되어있다.

```bash
$ npm i -g @nestjs/cli
$ nest new project-name
```

조금 더 선택적으로 nest를 실행하고 싶다면 core를 설치하면 된다.

```bash
npm i --save @nestjs/core @nestjs/common rxjs reflect-metadata
```

---
참조 : https://docs.nestjs.com<br>
참조 : https://velog.io/@hopsprings2/견고한-node.js-프로젝트-아키텍쳐-설계하기<br>
