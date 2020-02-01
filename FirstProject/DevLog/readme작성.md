# INSSA-client

- INSSA 프로젝트는 취미활동에 맞는 동호회를 찾고, 여가생활을 같이 즐길 사람들을 만나기 위한 웹 애플리케이션 입니다.

# Project Info

## 1. Get start

- 프로젝트를 `fork`, `clone` 이후, 아래를 순차로 실행함.

````bash
$ yarn install
$ yarn start
````

## 2.  Used Stack & Module

- React -  **Functional Component** 
- Typescript : TSX
- axios
- Design : [Ant Design]([https://ant.design](https://ant.design/)), [material-ui]([https://material-ui.com](https://material-ui.com/)), [fontawesome]([https://fontawesome.com](https://fontawesome.com/)), CSS3

## 3. Why we used this stack & module

- TypeScript
  - 모든 `data`들의 `type`을 정해줌 으로, JS를 단독으로 사용할 때 보다 컴파일 단계에서 오류를 포착 할 수 있다.
- React - Functional Component
  - 함수형 컴포넌트를 사용하면, class문법으로 정의한 컴포넌트보다 마운팅 속도에서 우위를 갖기때문에 `React Hooks` 를 이용하여 구현하고자 하였다.
- Axios : 편리함과 확장성을 위하여 사용, HTTP요청에 대한 **모듈화**적용
- React UI Library
  - View를 디자인하는데에있어서 빠른 UI구성과 완성도 높은 디자인을 구성하기 위하여 사용

## 4. Future Development Direction

#### Project

- `장소 예약 서비스` 및 이에 따른 `결제 모듈`추가
- 사업자 회원 서비스
- 모임 `일정` 추가

#### Client

- `ant Design` 및 `material UI`을 단일사용. 테마 확장 및 사용자화
- 기능 확장을 위한 `react Router`사용
- 조금 더 동적인 웹앱 구성