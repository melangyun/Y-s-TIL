# 6_200213-200219 User_Authentication_Front

1. Client Code를 fork받았다.

   - 일단 옮기려고 시작했는데, expo도 그렇고, 안드로이드 에뮬레이터도 그렇고, 모바일이라,
     `http://localhost/`가 먹지 않아서 개인의 `private ip`를 찾아 `localhost`자리에 넣어야 했다.

     ubuntu 에서는 `ip addr`을 하면 개인의 private port number가 나와서 연결이 되었다.
     사실 이 에러는 특별한 코드를 띄우지 않았고.. 그저 `Internet Error`를 띄울 뿐이라서 클라이언트와 서버의 연결이 미궁에 빠질것 같았으나....

     > 이번에도 **서치왕 성현님이**해결해주셨다.. 파하하.
     > 그 없이는.. 아무것도 못했을거야..

     

   - 안드로이드 에뮬레이터 또한.. 설치하는데 자잘한 에러가 있었으나..
     이 또한 수많은 구글링과 성현님의 캐리로 어떻게든 극복했다..
   
   - 실제로 코드가 돌아가기 까지 코딩보다도 *정말 많은 설정에러* 들이 있었고, **하기싫다**는 생각이 가득 들기 시작해서 많이 쳐졌던것같다.*(설정만 꼬박 이틀동안 헤메었던 것 같다.)*
   
     > ​	서버코드는 거의 완성형인데, 클라이언트라곤 어떻게든 못하겠어? 라고 생각했으나,,...
     > 모바일 설정만으로도 많이 지쳐서 쳐졌다..
   
     
   
   - EXPO를 실제로 구동해보니, 정말로 신기하고 대단하다는 생각이 많이 들었다.
   
2. 코드를 본격적으로 보기 전, mobex와 reactNative공부를 간단히 하였다.

   - 너무 간단한 설명들을 봐서 실제로 이해할수 있을까? 걱정을 많이했으나, 수지님과 대연님이 너무 친절히 설명해주셔서 *(생각보단)* 금방 *(과연?)* 이해 할 수 있던 것 같다.
   - 또, `axios`요청을 간단히 시작하고 끝낼 수 있을것 이라는 생각과는 다르게, 페이지를 새로 짜고 컴포넌트를 새로 구성하기 위해 **컴포넌트 구조를 파악하고 질문하는 시간**이 생각보다 굉장히 길었던 것 같다. *(하루 이상)*  

3. 로그인, 로그인 유지, 마이페이지 (로그아웃, 비밀번호 변경, 비밀번호 찾기)페이지를 만들고*(만들었다기 보단.. 있는 코드를 재활용-조립했다는 표현이 더 적절할것같다.)* 코딩을 하기 시작했다.

   - 로그인 유지를 먼저 시작했는데, 클라이언트 코드 뿐만 아니라, **서버코드** 에서 굉장히 많은 수정들이 있었다.
     **막연히 그렇겠지.. 하고 시작했던 코딩들이 클라이언트에서 받아보니 생각과 다른것들이 너무 많았기때문에..**
     데브로그가 조금 밀려서 디테일한 부분들은 잘 기억 나진 않지만, 여러가지 생각과는 달랐던 부분들이 많았다.

     - `jsonwebtoken`모듈로`secretKey`로 `signed`했던 부분들이, `react-Native`용 `jwt`모듈로 `verify`되지 않았다.
       일단 당연히 `jsonwebtoken`이겠지.. 하고 구동하는순간 *에러가 주루륵-* 올라가면서 `react-native`에서 사용 할 수 없다는 로그들이 나왔다.
       구글링을 통해 `react-native`에서 사용하는 `jwt`모듈들을 다운받았으나, `signed`된 것을 풀때 에러가 나지 않는것을 찾을 수 없었다.. *(아마도 verify 의 로직이 다른게 아니였을까..)*

     - `jwt`를 발급하여 `signed cookie`에 담아주고있었는데, 이 암호화를 또 클라이언트에서 풀지 못하였다.

       > 물론, 위 *cookie와 jwt*모두 사용할 수 있는 방안이 분명 있었을 것이나, 최소한 찾는 시간 대비 결과가 나오지 않아서, 우선 로그인을 할 수 있는 방안으로 하는 것을 택하였다.

       

     - 또, server요청에 모두 쿠키의`jwt`를 사용하여 `userId`를 받고있었는데, 내가 로그인유지에서 *많은 부분들을* 고민하느라 회원가입을 어서 만들어 내지 못해 server와 요청을 잇던 성현님과 수지님이 굉장히 불편하셨던것 같다*(서버에서의 userID하드코딩 -> 추후 에러로 이어짐 등.)*. 또, API문서로 사용하고 있던 `gitBook`의 무료이용기간이 만료되어 의사소통이 굉장히 어려움이 있던 듯 하다.

   - **`accessToken`이 만료되었을 때에 `client`에서 `accessToken`을 다시 요청해야하는 에러처리가 반드시 필요한데, 모든 `axios`요청마다 이 에러처리가 반드시 이루어져야 하는가?**에 대한 의문이 굉장히 많이 들었다. 그래서 회의시간에 쉬이 말하지 못하고 몇일을 고민하다가 결국에는 모든 요청마다 `accessToken`에 대한 에러처리가 필요하다고 말을 꺼내게 된 것같다.
     여기에 고민 + 구글링 하다가 팀원들과 함께 찾고 결론내린 방안들인데, *(차선책이긴 하지만... 확실히 아무 방편도 없는 것 보단 나은것같다. )*

     1.  앱이 구동될 때 마다`refreshToeken`으로 accessToken을 발급하는 요청을 무조건 보내준다.
        `refreshToken`이 유효한이상 `accessToken`은 재발급될것이다.
        만일 `refreshToken`이 만료된 경우 로그인 유지가 되지 않는다.

     2.  서버로 요청이 갔을때, `accessToken`을 검증하는 router를 만들어 `accessToken`을 검증하고, `accessToken`이 만료되었을때 이를 재발급받는 요청으로 `redirect`한다.

        > 이때, 클라이언트는 반드시 에러를 맞이하게 될것이나.... 이에대한 에러처리를 *시간이 남는다면* 이어서 하기로..하였다...
        > 앱스토어에 배포를 할 것이기 때문에, 에러처리가 반드시 이루어져야할것이다.
        >
        > ..개발할 때 몰랐던 버그들이 사람들이 사용하면서 쏟아지는것을 알고있기때문에..ㅠ 
        > 하지만, accessToken의 유효기간은 하루이며, 앱을 재구동할 때 마다 accessToken을 재발급받으니, 이러한 상황은 비교적 적지않을까 생각한다.

        

     3. 중복로그인 방지에 대한 걱정(?!) 도 꽤 오래했는데, 고민하다보니, *refreshToken*을 사용하게 되면 *accessToken*이 만료되면 자연스럽게 중복로그인이 되지 않는다는 것을 깨달았다.
        *(db에 refreshToken을 보관하고 있으므로, 자연스럽게 중복 로그인이 된다면 먼저 로그인한 refreshToken은 인증되지 않는다.)*

        놀랍게도 정말 많은 고민 끝에.. 알게되었기때문에 ...... 몇일 깊은 고민을 했던 것 같다.

     

   - 암호화된 `cookie`와 `jwt`를 클라이언트에서 해독하지 못했기때문에, 서버에서 `accessToken`을 발급 받을 때 마다 `react-native`의 **Async Storage**에 userInfo를 서버에서 재발급받아 업데이트 해주었다.

     - **Async Storage**는 기본적으로 *Pomise*를 반환하는데, 이때문에 에러를 굉장히 많이 마주하였다.

     > 사실, 에러의 시작은 내가 react 의 life-cycle의 많은 부분들을 잊었기 때문이었던것 같다.
     >
     > 변명을 잠깐 하자면, 2주 프로젝트때 client를 담당하였으나, 2주 프로젝트의 목표 중에 하나가, class형 component를 사용하지 않고 functional 한 react를 사용하는것이였기때문에... 최대한 이러한 상황을 지양하여 코딩하였고... 
     >
     > 다양한 상황을 마주하기에는 시간이 부족하였기때문에(기획 미숙으로 인한미구현).. 다양한 상황을 맞이하지 못하였던 것 같다.

     

     > 사실 아직도.. 죽어도 null값만 뿜어내는 *마이페이지*...
     > *root* 페이지에서 한번 state를 업데이트하고, 마이페이지 componentDidmount에서 다시 시도하는것으로..마무리하였지만 왜그런지는 아직도 잘 모르겠다..

     

     - 라이프사이클을 다시 공부하고, 코드를 적용하는데에도, mobex의 값을 inject하는데에 미숙하여 자잘한 에러들을 많이 마주했던 듯 했다.

       > 프로젝트 끝나고 리덕스를 꼭 공부해야지..!

       

     - 로그인 유지가 성공적으로 되고, 팀원 모두 회원가입 - 로그인 후 앱 개발을 하기 시작했다..(감동) 서버 코드도 알아서 token에서 UserId를 뽑아다가 사용하기 시작하였다.
     
     - 간단하지만 반드시 필요한, 이메일을 이용한 *로그아웃*과 *비밀번호 초기화* 를 구현하였다.
       원래 로그인 화면을 보기위해서는.. 강제로 안드로이드 스튜디오의 캐쉬를 지워야했는데 *(그렇게 되면 구동시간이 너무 길어져 너무 불편했다.)* 이것이 해소되어 너무 기뻤다.. 또 여기서 *React-navigation*을 공부하고 *(공부 했다기 보단, 에러를 내고 헤매고 질문을 했다는 표현이 더 가까운 것 같다.)*  신세계를 맞이하였다.. 세상에 이런 기능이!
     
   - react - native 와 mobex모두 생소했지만, 친절하신 수지님이 너무 잘 설명해주셔서 어떻게든 한것같다..*(잘 한지는 모르겠다..)*

4. `react-native`에서는.. 가상의 환경을 구축하는 것 자체로 시간이 오래걸렸고, 사소한 *human Error*로도 *붉은 줄*을 쥬르륵 - 올리며 랜더가 아예 되지 않아서.. 
   *뭐가 문제인지..* 띄워주지 않아 심플한 페이지를 몇개 짜는데에도 시간이 생각보다 *정말 -* 오래걸렸던 것 같다.

5. 이 작업들과 동시에 client에서 작업이 진행되며 필요한 server 코드들을 debugging 및 reafactoring하였다.

   - comment부분에서 *(간지나는)*페이지네이션 Module을 가져오셔서 `pagination`도 구현하였는데,
     spring에서 직접 페이지네이션 알고리즘을 구현했던것과는 달리, **TypeORM**은 공식페이지에서부터 pagination을 위한것들을 기능들을 지원하고 있기때문에 굉장히 간단했다.

     ````typescript
      const { postId, pagination }:{postId?: string, pagination?:string} = req.params;
             const postIdNumber:number = Number(postId);
             const paginationNumber:number = Number(pagination);
     		//몇번째 페이지가 필요한건지 param으로 받는다(0부터 시작)
             const nthPage = paginationNumber * 10;
     		//skip할 페이지 갯수를 구한다.
             const resultArr:Array<object> = await getRepository(Comment)
             // 옆에서 성현님이 본인 query문이라고 소유권을 주장하심
             // 사실 성현님 코드에서 페이지네이션만 넣었습니다.
                 .createQueryBuilder("comment")
                 .where("comment.postId = :id AND comment.status = :status", { id: postIdNumber, status: "Y" })
                 .leftJoinAndSelect("comment.user", "commentUser")
                 .select(["comment", "commentUser.id", "commentUser.nickname", "commentUser.Id", "commentUser.nickname", "commentUser.photoPath"])
                 .orderBy("comment.id", "DESC")
                 .skip(nthPage)//위에서 계산한 nthPage를 skip하고,
                 .take(10)// 10개를 가져온다.
                 .getMany();
     ````

     pagination 알고리즘과 달리 정말로 이렇게 간단해도 되는지 의심스러울 정도로 간단해서 진정으로 이게 일을 하는 코드인지 여러번 테스트 해본 것 같다.

   - 이외에도,  지도 마커를 뿌려주는 부분에서 정보가 더 필요하다고 해서 쿼리문을 고치다가, `inner View` 에서도 `*`를 쓸 수 있다는 사실을 알게되었다.
      *놀랍게도 여태까지 프로젝트를 하면서 항상 일일히 다 지정을 해주었었다는사실..*

     > 사실 질문하려고 들어갔던 kakaoTalk DB관련 opentalk방에서 주워듣고, 조인이 많이진 김에 적용해봤다..
     > 지금은 조금 TMI이긴 하지만,  `join on`조건에 넣게되면, 옵티마이저가 이를 판단하고 `where`절에서 들어가 일 하게 될 수 도 있다고 한다...! 쿼리문이 확연히 짧아졌으니 참고!

     

     ````mysql
     select 
     	jointable.*,
     	if(isnull(following_cat.userId) , false, true) as `isFollowing` 
     from ( 
         select innertable.*,
         photo.path as `catProfile`
         	from ( 
                 select
                 	id as `catId`,
                 	nickname as `catNickname`,
                 	address as `catAddress`,
                 	X(`location`) as `latitude`,
                 	Y(`location`) as `longitude`,
                 	description as `description` 
                 from cat 
             ) as `innertable`
         left join `photo` 
         on (innertable.catId  = photo.catId and photo.is_profile = 'Y') 
         where innertable.latitude <= ? 
         and innertable.latitude >= ? 
         and innertable.longitude <= ?
         and innertable.longitude >= ? 
     ) as `jointable` 
     left join `following_cat` 
     on (jointable.catId = following_cat.catId and following_cat.userId = ?) ;
     ````
     
     위 코드에서 `null`일 때에는 false로, 값이 있을 때에는 true로 boolean값으로 꺼내고 싶었는데, 막상 select 해오니 1과 0으로 나왔다.. 왜그런지는 모르겠지만, 코딩하는데 지장은 없으니 나중에 한번 찾아봐야겠다..
   
6. mobex의 store가 cat과 user두개로만 나누어져있어서 store 코드가 너무 길었다. 또, 처음에 기획대로 설정하였던 변수와 `function`들을 사용하지 않는것들이 존재해 어떤게 사용하고 사용하지 않는건지 , 구분이 가지않고 혼란했다.. 모든 store 무려 코드가 500줄 이상..! *(아직 기능이 다 안나왔음에도..)*

   - 클라이언트 작업을 하며 성현님과 이러한 부분에서 의견이 일치하여 front부분을 담당하셨던 수지님과 대연님께 미팅시간에 건의하기로 하였다.
   - 두분 다 *약간의 설득 시간이 필요했지만* 결국 동의해 주셨고  
     - AuthStore, CatStore, HelperStore, MapStore, PostStore, ReportStore, UserStore로 회의 끝에 나누기로 하였다,
     - 여태까지의 코드를 수지님과 대연님이 refactoring하는동안 나와 성현님은 server에서 필요한 디버깅과 기능을 추가했다. 성현님은 소켓부분을 공부하기 시작하셨다.

   > 사실 스토어가 세분화부분에서 조금 부족해  *어디에 뭐가 있는지* 찾기 힘들었었다.
   >  스토어를 나누자는 나의 주장에 대연님이 그 스토어를 나누게 된다면 하나 또는 두개의 기능만 있을텐데 나누는게 맞을까요..?라고 말씀하셨을때 뭐라고 적절한 말을 찾기 힘들었었다.
   > 그때 성현님이 스토어에 하나만 있어서 누가 봐도 어디에 어떤기능이 구현되어있는지 찾을수 있게 하는것이 좋을것 같다고 말씀해주셔서 굉장히 인상깊었다.
   >
   > 또 지금 이걸 적으면서 생각해보았을 때 앱의 확장측면에서도 조금 번거로워도 나누는게 더 올바른 선택이였다고 생각한다.

   

7. mypage의 로그인,로그아웃, 비밀번호찾기, 비밀번호 변경기능을 완성해가고 followrList를 어떻게 해야할까 고민을 시작한 차에, 소켓부분의 server 코드에 고민이 많으셨던 성현님이 오피스아워에 *두현님* 께 프로젝트를 들고갔다가 *router*에 대하여 대차게 까이고 오셨다.. 두현님이 지적한 부분은 정말 당연하면서도 생각하지도 못했던 부분이였는데,..

   >  우리가 구조에 있어서 cheat Sheet처럼 썼던 코드들이 우리기수에 그래도 신뢰도가 굉장히 높은 분(들)의 코드였기 때문이다.
   > 생각해보면 정말 당연한 지적들인데, 스스로 생각하고 고칠 생각을 하지 못하고 너무 그분들의 코드만 신봉했던것에 대해 반성한다.  

   

   - mvc패턴의 부재 -> 현재 router에서 컨트롤러에서 모델의 기능까지 들어가있는데, 분리가 필요함
   - db Status에 대해 ts의 eenum기능을 활용할것.
   - 인증 미들웨어 만들기 -> 이부분은 이미 오래전에 만들어두었는데, 성현님이 포스트맨으로 테스트를 해본다고 주석을 달아놓아 보지 못하신 듯 하다.

   아무튼, router에서 모든 코드가 있는 구조에서 mvc모델로 리펙토링 하려면 성현님과 꽤 많은 소통과 적절한 역할 분담이 필요할것이다.
   또, 정말 엄격한 MVC패턴을 사용했던 SPRING으로 진행했던 프로젝트를 다시 열어보았을 때, *(node 환경과는 정말 다르지만, MVC패턴의 참고용으로..)* 우리의 현재 프로젝트가 너무 *에러처리에 대해서 통일된 처리가 있지 않다*고 느끼었다. 그래서 추가적으로 *에러처리*에 대한 공부와 리펙토링이 필요할것같다. 내일부터는 위에 내용으로 리펙토링을 진행할것같다..!

제발 데브로그좀 밀리지말고 그때그때 써야지 이거 쓰는데 두시간 넘게걸림ㅠㅠ..



