typescript는 Js의 superset!
typescript 는 프로그래밍 언어인데, 자바스크립트처럼 생겼고, 컴파일하면 Js로 컴파일됨! 
typescript를 사용하는 이유 - Js가 갖고있지 않은 규칙들을 갖고있기 때문에



- tsconfig.json을 만든다

  ````json
  //이 파일에 TypeScript 에게 어떻게 JS로 변환하는지 알려주면서 몇몇 옵션을 줄것임
  {
      "compilerOptions": {
          //노드 모듈의 사용
          "module": "commonjs",
          //어떤 버전의 Js로 컴파일 되는지
          "target": "ES2015",
          //sourcemap 처리를 하고싶은지
          "sourceMap": true,
          //컴파일된 경로
          "outDir": "idst"
      },
      //어떤 파일들이 컴파일 과정에 포함되는지 TypeScript에게 알려주어야함
      "include": ["index.ts"],
      "exclude": ["node_modules1"]
  }
  ````

- `tsc`를 터미널에 입력하면 위 설정에 맞게 js파일로 컴파일된다!
  **Node.js는 TypeScript를 이해하지 못하기때문에, 일반적인 JS코드로 컴파일 하는 작업이 반드시 필요하다.**

- package.json

  ````json
   {
       "scripts" : {
      	"start" : "node index.js",
      	"prestart" : "tsc"
    	}
    }
  ````

- `yarn add tsc-watch --dev` 

- package.json

  ````json
   {
       "scripts" : {
      	"start" : "tsc-watch --onSuccess \"node dist/index.js\""
    	}
    }
  ````

- **typescript code**

  ````typescript
  const sayHi = (name:string, age:number, gender:string):void => {
      console.log(`Hello ${name}, you are ${age}, you are a ${gender}`);
  }
  
  sayHi('Nicolas' , 27 , 'male');
  
  //타입스크립트 또한 모듈화 ? 버그
  export {};
  ````

- ts example

  ````typescript
  const person = {
      name : "nicloas",
      gender : "male",
      age : 22
  }
  ````

  