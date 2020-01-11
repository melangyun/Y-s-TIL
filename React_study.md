# 1. 리액트 시작
- Vs Code 확장프로그램 설치
  - ESLint
  - Reactjs Code Snippets
    리액트 컴포넌트 및 라이프사이클 함수를 작성할 때 단축 단어를 사용하여 간편하게 코드를 자동으로 생성해 낼 수 있는 코드 스니펫 모음
  - Prettier-Code formatter

# 2. JSX

## 2.1 코드 이해하기

````javascript
import React from 'react'
````

- 모듈을 불러와서 사용하는 것은 원래 브라우저에는 없던 기능이나, 브라우저가 아닌 환경에서 자바스크립트를 실행할 수 있게 해 주는 환경인 Node.js에서 지원하는 기능이다.
- 이러한 기능을 브라우저에서도 사용하기 위해 **번들러(Bundler)**를 사용한다.(파일을 묶듯이 연결함)
  대표적인 번들러로는 *웹팩, Parcel, browserify*라는 도구들이 있으며, 각 도구마다 특성이 다르다. **리액트에서는 주로 웹팩을 사용하는 추세이다.**(편의성과 확장성이 뛰어나기 때문)
- 웹팩을 사용하면 SVG파일과 CSS 파일도 불러와 사용할 수 있다.
  이렇게 파일들을 불러오는 것은 웹팩의 로더(loader)라는 기능이 담당한다.
  - css-loader : CSS파일을 불러올 수 있음.
  - file-loader : 웹 폰트나 미디어 파일 등을 불러올 수 있게 해줌
  - babel-loader :자바스크립트 파일들을 불러오면서 최신 자바스크립트 문법을 ㅗ작성된 코드를 바벨이라는 도구를 이용하여 ES5 문법으로 변환해준다.(구버전 브라우저를 위함)

## 2.2 JSX란?

자바스크립트의 확장 문법이며 XML과 매우 비슷하게 생겼다. **이런 형식으로 작성한 코드는 브라우저에서 실행되기 전에 코드가 번들링되는 과정에서 바벨을 사용하여 일반 자바스크립트 형태의 코드로 변환됨**

````jsx
function App(){
    return(
    	<div>
       		Hello <b>react</b>
        </div>
    )
}

export default App;
````

이렇게 작성된 코드는 다음과 같이 변환됨

````javascript
function App(){
    return React.createElement("div", null, "Hello", React.createElement("b",null,"react"))
}
````

## 2.3 JSX의 장점

- 보기 쉽고 익숙하다( Vanilla script 와 html 태그 의 가독성 차이)
- 더욱 높은 활용도 - 컴포넌트를 HTML태그를 쓰듯이 그냥 작성할 수 있다.

## 2.4 JSX문법

### 2.4.1 감싸인 요소

- Virtual DOM에서 컴포넌트 변화를 감지해 낼 때 효율적으로 비교할 수 있도록 컴포넌트 내부는 하나의 DOM트리 구조로 이루어져야 한다는 규칙이 있다.
- div요소를 사용하고 싶지 않을때는 리액트  v16이상부터 도입된 Fragment 라는 기능을 사용하면 된다.

````jsx
import React, { Fragment } from 'react';

function App(){
    return(
    	<Fragment>
        	<h1>리액트 안녕!</h1>
            <h2>잘 작동하니?</h2>
        </Fragment>
    )
}

export default App;
````

위 와 같은 코드는 아래와도 같은 형태로도 표현 할 수 있다.

````jsx
import React, { Fragment } from 'react';

function App(){
    return(
    	<>
        	<h1>리액트 안녕!</h1>
            <h2>잘 작동하니?</h2>
        </>
    )
}

export default App;
````

### 2.4.2 자바스크립트 표현

````jsx
import React, { Fragment } from 'react';

function App(){
    const name = '리액트';
    return(
    	<>
        	<h1>{name} 안녕!</h1>
            <h2>잘 작동하니?</h2>
        </>
    )
}

export default App;
````

### 2.4.3 if 문 대신 조건부 연산자

JSX 내부의 Js표현식에서 if문을 사용할 수는 없다. 하지만 조건에 다라 다른 내용을 랜더링 해야할 때는 JSX 밖에서 if문을 사용하여 사전에 값을 설정하거나, `{ }` 안에 조건부 연산자`(삼항연산자)`를 사용하면 된다.

````jsx
import React from 'react';

function App(){
    const name = "리액트";
    return (
        <div>
    	{
            name === '리액트' ?
            (<h1>리액트입니다.</h1>) : (<h2>리액트가 아닙니다.</h2>)
        }
       	</div>
    );
}

export default App;
````

### 2.4.4 AND 연산자(&&)를 사용한 조건부 랜더링

````jsx
import React from 'react';

function App(){
    const name = '뤼액트';
    return <div>{name === '리액트' ? <h1>리액트입니다.</h1> : null } </div>;
}

export default App;
````

- **null로 랜더링 시 아무것도 랜더링 되지 않는다.**

````jsx
import React from 'react';

function App(){
    const name = '뤼액트';
    return <div> {name === '리액트' && <h1>리액트입니다.</h1> } </div>;
}

export default App;
````

- &&연산자로 조건부 렌더링을 할 수 있는 이유는 리액트에서 false를 랜더링 할 때는 null과 마찬가지로 아무것도 나타나지 않기 때문이다. 
  **단, falsy한 값인 0은 예외적으로 화면에 나타난다.**

````jsx
const number = 0;
return number && <div>내용</div>
    //이러한 코드는 화면에 숫자 0 을 보여준다.
````

- JSX작성시 괄호로 감쌀 때도 있고, 그렇지 않을 때도 있다. 주로 JSX를 여러 줄로 작성할 때 괄호로 감싸고, 한 줄로 표현할 수 있는 JSX는 감싸지 않는다. *필수 사항이 아님*

### 2.4.5 undefined를 렌더링 하지 않기

리액트 컴포넌트에서는 함수에서 undefined만 반환하여 렌더링 하는 상황을 만들면 안된다. 아래와 같은 코드는 오류를 발생시킴

````jsx
import React from 'react';
import './App.css';

function App(){
    const name = undefined;
    return name;
}
export default App;
````

​	*App(...) : Nothing was retruned from render. This usually means a return statement is missing. Or, to render nothing, render null.*

어떤 값이 undefined 일 수 도 있다면 OR(||)연산자를 사용하면 해당 값이 undefined일 때 사용할 값을 지정할 수 있으므로 간단하게 오류를 방지할 수 있다.

````jsx
import React from 'react';
import './App.css';

function App(){
    const name = undefined;
    return name || '값이 undefined입니다.';
}
export default App;
````

**반면, JSX 내부에서 undefined를 렌더링 하는 것은 괜찮다.**

````jsx
import React from 'react';
import './App.css';

function App(){
    const name = undefined;
    return <div>{name}</div>;
}
export default App;
````

**undefined일 때 보여주고 싶은 문구가 있다면 다음과 같이 코드를 작성하면 된다.**

````jsx
import React from 'react';
import './App.css';

function App(){
    const name = undefined;
    return <div>{name || '리액트'}</div>;
}
export default App;
````

### 2.4.6 인라인 스타일링

리액트에서 DOM요소에 스타일을 적용할 때는 문자열 형태로 넣는 것이 아니라 객체 형태로 넣어 주어야 한다.
스타일 이름중에서 background-color 처럼 - 문자가 포함되는 이름이 있다면 **카멜 표기법**으로 작성하면된다.

````jsx
import React from 'react';

function App(){
    const name = '리액트';
    const style = {
        backgroundColor : 'black',
        color : 'aqua',
        fontSize : '48px',
        fontWeight : 'bold',
        padding : 16 //단위를 생략하면 px로 저장됨
    }
    return <div style={style}>{name}</div>
}
export default App;
````

혹은 다음과 같이 작성하면 된다.

````jsx
import React from 'react';

function App(){
    const name = '리액트';
    return <div 
               style={{
        backgroundColor : 'black',
        color : 'aqua',
        fontSize : '48px',
        fontWeight : 'bold',
        padding : 16 //단위를 생략하면 px로 저장됨
    }}>
        {name}
    </div>
}
export default App;
````

### 2.4.7 class 대신 className

````jsx
import React from 'react';
import './App.css';

function App(){
    const name = '리액트';
    return <div className="react">{name}</div>
}

export default App;
````

### 2.4.8  꼭 닫아야 하는 태그

태그를 닫지 않으면 오류가 발생한다. **self-closing태그 표기**

````jsx
import React from 'react';
import './App.css';

function App(){
    const name = '리액트';
    return (
    	<>
        	<input></input>
        	<input/>
        </>
    )
}

export default App;
````

### 2.4.9 주석

````jsx
import React from 'react';
import './App.css';

function App(){
    const name = "리액트";
    return (
    	<>
        {/*주석은 이렇게 작성합니다.*/}
        <div 
            className = "react" // 시작 태그를 여러 줄로 작성하게 된다면 여기에 주석을 작성 할 수 있습니다.
            >
            {name}
        </div>
        //하지만 이런 주석이나
        /*이런 주석은 페이지에 그대로 나탄게 됩니다.*/
        </>
    );
}
````

## 2.5 ESLint 와 Prettier적용하기

### 2.5.1 ESLint

EsLint는 코드를 작성할 때 실수를 하면 에러 혹은 경고메세지를 VS Code 에디터에서 바로 확인할 수 있게 해준다.초록 줄이 그진 코드는 무시해도 좋지만(지양 필요) 빨간줄은 치명적이므로 반드시 고쳐주어야한다.

### 2.5.2 Prettier(80p) 프리티어

VS Code에서 F1을 누르고 format이라고 입력한 다음 엔터를 누르면 적용됨

# 3. 컴포넌트

