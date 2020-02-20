# 5_200208-200212_User Authentication Part

1. 대망의 유저 로그인 및 토큰 부분을 공부하기 시작한다
   괜히 내가 한다고 했나 급격하게 후회가 되지만 하다 보면 어떻게든 되겠지...
   내게는 구글 님이 계시니....아래 자료들을 정독하였음!
   
   | 참조사이트                                                   | 메모 |
   | ------------------------------------------------------------ | ---- |
   | [세션 기반 인증 방식과 토큰 기반 인증(JWT)](https://yonghyunlee.gitlab.io/node/jwt/) |      |
   | [JWT(Json Web Token)을 이용한 모바일 인증](http://throughkim.kr/2017/03/14/Jwt/) |      |
   | [JWT를 구현하면서 마주치게 되는 고민들](https://swalloow.github.io/implement-jwt) |      |
   | [jwt.io]([https://jwt.io](https://jwt.io/))                  |      |
   | [Refresh Token 과 Sliding Sessions를 활용한 JWT](https://blog.ull.im/engineering/2019/02/07/jwt-strategy.html) |      |
   | [생활코딩 OAuth2.0](https://www.youtube.com/watch?v=hm2r6LtUbk8&list=PLuHgQVnccGMA4guyznDlykFJh28_R08Q-) |      |
   | [Node.js_JWT기반으로 사용자 인증 구현하기](https://victorydntmd.tistory.com/116) |      |
   | [login-api_깃허브 참조코드](https://github.com/a-mean-blogger/login-api/blob/459a532d67226667ca82cfce9cdc213c33ac5123/api/auth.js) |      |
   | [노드-기능-알아보기](https://happyer16.tistory.com/entry/3-노드-기능-알아보기) |      |
   
2. 사용자에게 비밀번호를 받으면 암호화를 하였다.

   - ts 타입 에러가 자꾸만 나서 type script 를 지원하는 여러 모듈들을 설치하고 지우고 여러가지 코드를 참조하다가 결국에는 `crypto` 내장 모듈에서 ts에 맞추어 하는 방법을 찾았다.
     비슷한 기능이라면 굳이 확장 모듈을 추가적으로 설치하지 않는 것이 더 좋을 것이라고 생각했기 때문에 ts용 모듈이나 다른 보편적인 모듈들 보다 내장 모듈로 최대한 사용하는 것이 나을 것이라고 생각했다.

   - 단순히 해싱 -> 저장보다 `crypto.randomBytes`를 이용해  유저 마다 각기 다른`salt`를 만들어 userTable에 Insert 해주었다. 비밀번호 확인이 필요한 순간마다 user ID로  db에서 유저의 salt를 찾아와 같은 로직 으로 암호화 후 db의 비밀번호와 비교해 주는 방식으로 암호화를 모두 적용하였다.

     > 이 로그를 쓰면서 `change password`시에 새로운 비밀번호는 암호화 하지 않았다는 사실이 생각나 후딱 암호화를 하고 왔다..

     

3. 우선 일반적인 jwt를 발급하는 코드를 짰다.

   - accessToken과 refreshToken을 모두 이용하는 방식으로 코딩 하고 싶었으나.. 예시 코드가 너무 부족했다.
   - 여러 자료들을 보다가 우선.. 내가 `jwt`자체도 활용해본 경험이 적다는 것을 깨닫고 일반적인 jwt를 사용하여 로그인 하는 코드를 작성하였다.
   - 또, 발급해 줄 jwt를 어디에 넣어 줄 지에 대한 것도 많이 혼란했기 때문에 정말로 token을 발급하고 `response`에 담아 보내주기 만 하였다.
     - 안드로이드는 `SharedPreferences` 또는  `key store`를 사용하는 것이 안전하고, IOS의 경우 `key Chain`을 사용하는 것이 안전하다고 하는데 사실 그 둘 중 어느 것에 대한 지식도 적고 확신도 적었기 때문에..
       그리고 사실 *refresh Token을 엄청나게 어렵게 생각하고 있었기 때문에.. 할 것이 많다는 생각에 ..*   
       어떻게 해야 할 지 길을 잃었었다.

4. refresh Toekn을 발급하는 코드를 작성함!

   - 내가 찾은 예시 코드가 너무 적었고, 개념 만으로 보안의 *(내가 생각하기엔 )*중요한 부분을 코드로 짜버리는 것에 대한 확신이 없었다.
     그래서 하루 종일 refresh Token에 대한 개념을 뒤적이고 코드를 찾았던 것 같다.

   - 한 유투브 강의를 보았는데, 우리와 사용 스택이 너무 달라 코드를 이해하는 것이 어려웠다. 
     boiler poject의 확장 모듈들 또한 스택적으로 너무 달랐고, 여러 시도 끝에 우리 코드에 결합 할 수 없다고 생각하고 ..*절망감에 빠져들었다..* 하루 종일 무언가 찾고 계속 시도했는데 하면 할수록 이해가 더욱 더 안되는 것 같고 *미궁에 빠지는 것 같았다.*

   -  이때 `amazon`에 사진업로드 파트를 진행하고 있는 성현님의 역할이 끝나가..
     

     > 성현님은 서진 업로드를 다 하는 동안 나는 무엇을 하고 있었는지..ㅠㅠ

     

     애꿎은 성현님에게 도움을 요청하면서 괜히 궁시렁 궁시렁 거렸던거 같다..ㅠㅠㅠ 왜 코드가 안나오냐고.....;(

   - 개념을 알려 드렸더니 그냥 개념 그대로 코딩을 하면 되는 것이 아니냐,
     고 하셔서 정말이지 나는..
     정말이지

     > 나는 정말 바보 같았다는 생각과 함께 머리를 한 대 맞은 것 같았다.

     ㅠㅠ

   - 아.. 왜 나는 refresh Token에 대한 개념들을 얼마나 많이 보았는데 왜 개념 그대로 코딩해 볼 생각은 해보지 않았을까?

   - 그래서 그대로 코딩을 할 생각을 하며 이것 저것 해보고 있었는데 성현님이 바로 참조 코드들과 유투브 강의까지 찾아주셨다.. *거의 다 떠먹여 주심..*

     > 나는 바보야 정말로.. 내가 얼마나 구글링을 허술하게 하고 많은 자료들을 놓쳤는지..!

     영어 자료를 열심히 본다고 본 것 같은데 사실 열심히 보지 않은 것 같았다.

     > 조급할수록 얕게 많은 것을 보려고 하지 말고 조금만 더 천천히 꼼꼼히 볼껄..!

     

   - refresh Token에 대한 공부를 하고 코드를 찾는데 *믿을 수 없지만* 하루가 꼬박 가고 실제로 `refresh Token`과 `access Token` 을 구현하는 동안 [JWT Authentication Tutorial](https://www.youtube.com/watch?v=mbsmsi7l3r4)  강의를 함께 들은 성현님이 인증용 서버 분리를 시작하였다.
     **그리고 하루도 넘게 헤메었는데, 막상 구현하기 시작하니까.. 생각보다 정말 간단해서 허무하기 까지 했다..**

     > 비교적 짧은 유효 시간을 갖는 accessToken은 실질적인 로그인 역할을 하며, 긴 유효 시간을 갖는 refresh Token은 accessToken을 재발급 해 주는 역할을 한다.

     

   - 성현님과 여러 논의를 통해 결국 `mobile cookie`에 token을 저장하는 것으로 충분할 것으로 결론 내렸다.
     애초에 보안이 (비교적으로)크게 중요하지 않은 애플리케이션 이기도 하고, 사실, 로그인의 보안에 `keyChain`으로 관리할 만큼 로그인 절차가 까다롭지 않기 때문이다. 또한 `cookie`도 암호화 절차가 있으며, `token`도 암호화를 하기 때문에 충분할 것이라는 결론을 내렸다. 

     > 사실.. client에 할당된 task가 비교적 더 많고 어려운 만큼 server 에서 추가적인 것을 욕심낼 수록 시간 내에 bareMinimum을 구현하지 못할 것 이라는 부담감도 있기도 했기 때문이다.

     

   - 이후 test또한 잘 되었고, userId가 필요한 부분을 모두 cookie와 jwt를 복호화 하여 사용하는 코드로 모두 리펙토링 하였다.

   - 또한 application자체가 모두 로그인 유저를 대상으로 하기 때문에, jwt 복호화 에러 처리(만료된 Token 에 대한 확인 과정) 를 모든 요청마다 거치기엔 코드적인 효율성이 너무나 낮기 때문에 jwt 유효성 검사에 대한 라우터를 작성하여 이 라우터를 거치게 하였다.
     **하지만, 회원 가입의 sign up에 관련된 요청들은 당연히 유저가 token을 갖고 있지 않으므로 (기존 user router 에서 signup router로 ) router를 분리하였다. (token에 대한 유효성 검사를 거치지 않는 라우팅을 위해)**

     >  라우터의 직접적인 구성 또한 정말 좋은 경험이었던 것 같다.

     

   - 아침에 일어났는데, 우리가 회원가입 시에 email은 unique하게 받으면서, 막상 email확인에 대한 서버 api가 전혀 존재하지 않는다는 것을 깨달았다.

   - 또, java로 프로젝트를 할 때 인증 메일을 보내는 것이 어렵지 않았다는 기억이 났고 *(오히려 정말 쉬운 기능 중 하나였다.)* 메일이 유효한가(아직 db에 저장되지 않은 메일인가)를 확인하는 로직과 함께 이메일 인증을 함께 진행 하는 것이 좋겠다는 생각이 들었다. *이메일 인증은 당장 `advanced session`에 있으므로 욕심 같기도 했지만.. spring때에도 그리 나쁜 기억은 아니 였기 때문에 일단 도전해보는 것 도 좋겠다는 생각을 하였다.*

   - 검색해보니, `nodemailer`로 정말로 간단히, 빠르게 *(심지어 에러도 단 한번도 나지 않고..)* 메일을 보낼 수 있었고, 아침 stand up meeting때 팀원들에게 건의 해 이러한 로직을 추가하기로 하였다!

   - 임의 문자열을 생성해 `get`요청을 보낼 것인가 혹은 `cookie`에 담아 클라이언트에서 인증을 해줄 것 인가 에 대한 논의가 있었고,  현재 우리에게는 사용자 경험보다는, 구현이 우선이므로, 구현할 내용이 적은 `cookie`에 담아 클라이언트에서 인증하는 방식을 선택하게 되었다. 

     >  인증 email UI를 잠시 잠깐 짧은 HTML과 CSS로 구현 하면서..잠시 잠깐 행복했다..

     

   - 자잘한 debugging들과 client요청에 대한 코딩들이 있었고, 서버 코드는 오늘부로 크게 마무리될 것 같다.
     우리 프로젝트는 서버에서 크게 어려운 기능이 없었기 때문에 생각보다 더 빡빡하지 않게 끝난 것 같다.

     

오늘 남은 시간 동안 client의 코드들을 보며 공부하는 시간을 갖고, 내일 client를 담당하는 팀원들에게 질문들을 하며,  server에 요청을 날리고 받는 부분들을 작업할 것 같다.
client의 UI와 요청들이 크게 마무리되면 server로 다시 돌아와 소켓과 `app push alarm`부분을 진행하지 않을까 한다.

서버 코드의 *(고작이지만)* 베어미니멈을 완료하니 시원섭섭하기도 하면서 정말로 배운 것이 많았던 것 같다.
