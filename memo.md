# 자잘한 메모들

## JS문법

- Object.values 하면, values값만 return한다.

## Linux

- sudo apt-get update

- sudo apt-get autoclean

- sudo apt-get clean

- sudo apt-get autoremove

- vim '파일명' : vim이라는 에디터 안에서 돌아감!

- 잠금화면 배경화면 설정
  터미널에 code /usr/share/gnome-shell/theme/ubuntu.css
  입력시 vs코드 에디터에 css파일에 출력됨 id가 \#lockDialogGroup인 부분을 찾아서 수정!

  - 원본

    ```css
    #lockDialogGroup {
        background: #596275 url(resource:///org/gnome/shell/theme/noise-texture.png);
      background-repeat: repeat;
    }
    ```

    수정본

    ```css
    #lockDialogGroup{
        background: #596275 url(file://`${경로}`);
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center; 
    }
    ```

  CSS수정본 모두 주석으로 이름달았음(`/*이름*/` )
  
- 경로를 GUI로 켜기 **nautilus**

## npm

- npm : js기반 코드를 재사용하고 공유하기 위함.
- npm list -g --depth = 0
- npm init 
  npm으로 package를 관리하기 위함이다. Init을 하면 npm에 의존하는 프로젝트를 만든다는 것이며, package.json이 생성된다.
- npm install express --save
  --save옵션 : 프로젝트가 의존하고 있는 package목록에 넣고, 이 프로젝트를 받는 사람이 이것을 설치할 수 있게 해준다.
  모듈 설치시 수많은 다른 모듈들 또한 함께 설치되는데, 이는 설치한 모듈들이 의존하고 있는 또다른 모듈들이다. npm이 자동설치 및 관리한다.
- npm install nodemon --save
  노드몬 설치
- -g 글로벌 설치
- -S 프로젝트 내에서의 설치
- body-parser
  npm install body-parser --save
- cors설치
  npm install cors
- 제스트
  npm i -D jest
- -D : 개발 의존성 설치!
- **npm install pm2 -g**
  **pm2 start app.js** 로 실행
  **pm2 start main.js**
  **pm2 monit** 를 실행시키면 pm2로 실행되고 있는 프로그램들이 보인다.
  **pm2 list** 를 하면 실행중인 리스트가 보이고, name을 확인하여 pm2 [name] stop하면 꺼진다.
  **pm2 start main.js --watch** 이렇게 실행하면 파일이 수정 될 때 마다 재실행됨!
  **pm2 log** 문제점이 있다면 문제점을 바로 보여줌!
- **npm install -g yarn**

## GIT

- git pull remote master

- git remote add pair(별칭) <url>

- git --help

- git pull 시에는 별 다른 권한 없이 코드를 가져올 수 있다.
  깃허브에 코드를 올렸다는 것 자체가 코드 공개를 시사하는 것 이기 때문이다.
  
- git pull pair master

- git push origin master

- **Git ignore 설정**

  1. ```javascript
     //.gitignore 파일을 생성한다.
     $touch .gitignore
     // .gitignore은 숨김파일이므로 아래의 2가지 방법으로 제대로 생성됐는지를 확인한다.
     $la
     $ls -a
     //.gitignore 파일을 수정한다.
     $vi. gitignore
     ```