# 4_200207_Router code 80% complete

몇 일 동안 정말로 정신이 없어서 dev-log가 많이 밀렸다.
일단 이전에 dev-log에 작성하였던 entity 코드들도 에러가 정말 많았다는 것을 알게 되었고, entity코드들을 얼마나 많이 바꾸었는지 모르겠다... 눈물이 줄줄..
지금은 **로그인, 개인정보 암호화, 사진 업로드, 배포 부분**을 제외하고 이외 라우터 코드들 작성과 API문서들 정리를 완료하였다.
음..typeORM 공식 문서 만 보고 알 수 없었던 수많은 에러들과 마주하고 고통 받은 나날들..

1. typeORM에서 쿼리를 작성하는 방법을 크게 3 가지로 사용한 것 같다.

   1. **raw query**를 이용한 방법
      형태는 다음과 같다.

      ````typescript
      const reuslt = await entityManager
      	.query("SELECT * FROM cat WHERE cat.id = ? ", [catId])
      ````

      ****

      **코드 활용**

      client 에서 *북서, 남동 위도와 경도*를 보내주면 **네모 공간 데이터**로 나누어 안에 존재하는 데이터들을 불러오는 쿼리문을 작성하였다.
      *query Builder로 최대한 많은 부분들을 활용하려고 했으나, `geometry`에 관련된 부분들은 공식 문서에서 내용 또한 너무 빈약했다고 느껴졌고, error에 대한 답안 또한 너무나 찾기 어려웠기 때문에, `raw-query`를 작성하는 법을 찾아  이용하였다..*
      또, 아래 쿼리는 **[db의 Point자료형에서 위-경도 받아오기](https://webinformation.tistory.com/55)** 를 활용하였다.

      ````typescript
       const result:Array<object> = await getConnection()
                  .query(
                      "select * 
      				from (
                      	select 
                      		id as `catId`, 
                      		nickname as `catNickname` , 
                      		X(`location`) as `latitude`, 
      						Y(`location`) as `longitude` 
                  		from cat) as `innertable` 
                      where innertable.latitude >= ? 
                      and innertable.latitude <= ?
                      and innertable.longitude >= ?
                      and innertable.longitude <= ? ;",
                  [
                     point.startLatitude, 
                     point.endLatitude, 
                     point.startLongitude,
                     point.endLongitude
                   ]
      );
      //""를 쓰면 엔터를 치면 안되지만, 여기에선 가독성을 위해 엔터로 정리함
      ````

   2. **object를 이용한 방법**
      entity에 관계를 지정해주었고, object자체로 query를 짤 수 있다.
      sequilze의 문법과 비슷했기 때문에 접근하기 쉽고 직관적이라 초반 코드를 모두 이런 방식으로 작성하였다.

      > *(하지만, 결과적으로 DB에 여러 번 접근해야 하기 때문에 비효율적이라는 결론이었고, typeORM github_issue에서 이러한 형식보단, queryBuilder의 사용을 적극 권장하고 있기 때문에, 모든 CRUD부분을 **queryBuilder**의 형식으로 전환하였다.)*

      ​	하지만, db의 편의성을 위해 작성한 index.ts의 테스트user 코드 까지는 아직 refactoring되지 못하였다. 
      ​	이 부분은 추후에 리펙토링 하여 **admin**계정으로 활용 할 수 있을 것 같다.

      ````typescript
      const user:User = new User();
      user.nickname = "testUser";
      user.password = "1234";
      user.email = "admin@codestates.com";
      user.status = "Y";
      const testUser:User = await User.save(user);
      if (!testUser) {
          console.log("Failed to save user.");
          return;
      }
      
      // * cat
      const cat:Cat = new Cat();
      cat.description = "test용 고양이입니다.";
      cat.location = new wkx.Point(1, 2).toWkt();
      cat.nickname = "devCat";
      cat.user = testUser;
      //이런식으로 user object자체를 user 의 input으로 활용할 수 있다.
      cat.status = "Y";
      cat.rainbow = JSON.stringify({
          Y: 0, YDate: null, N: 0, NDate: null,
      });
      cat.cut = JSON.stringify({
          Y: 0, N: 0, unknown: 0,
      });
      
      const devCat:Cat = await Cat.save(cat);
      if (!devCat) {
          console.log("Failed to save cat.");
          return;
      }
      ````

   3. **query Builder이용**
      query-builder를 이용하면, query를 조금 더 직관적으로 접근할 수 있을까? 
      사실, typeORM을 사용하며 발생하는 모든 CRUD부분 issue의 답변이 `queryBuilder`이였고, 공식 문서 또한 그랬기 때문에 `query-builder`를 사용한 것이지, 사실 이것을 사용함으로서의 이점은 아직 까지도 잘 모르겠다.

      > *아직 까지도 나는 그냥.. `raw-query`문이 훨씬 쉽기 때문에..그저 고통이었던 `queryBuilder`의 사용.. 
      > 쓰다 보면, 익숙해지고, 익숙해지면 편해지지 않을까 했는데 **적어도 나한테는** 전혀 그렇지 않았다...^^..;; 
      > 끝까지 헷갈리고 어려웠던 건, 내 뇌의 문제인가?*

      ````typescript
      const returnObj:Comment|undefined = await getRepository(Comment)
      	.createQueryBuilder("comment")
      	.where("comment.id = :id AND comment.status = :status",
         		    { id: commentId, status: "Y" })
      	.leftJoinAndSelect("comment.user", "commentUser")
      	.select(["comment", 
                   "commentUser.id", 
                   "commentUser.nickname", 
                   "commentUser.photo_path"])
      	.getOne();
      //조인의 관계가 조금 더 직관적으로 보일 수는 있을것같다.
      
      const result:UpdateResult = await getConnection().createQueryBuilder()
      	.update(Comment)
      	.set({ status: "D" })
      	.where({ id: commentId })
      	.execute();
      
      if (result.raw.changedRows === 1) {
          res.status(200).send({ deleteStatus: "Y", message: "Successfully deleted post" });
          return;
      }
      res.status(404).send("Deleting comment has failed");
      ````

2. **API문서의 전면 수정**

   우리가 API문서를 작성하고 맞이한 몇 가지 문제가 있었다.
   앞으로의 프로젝트에서는 아래 부분들을 보완하고 같은 문제에 부딪히지 않도록 최대한 노력해야겠다.

   1. Client측에서 작성한 Component기준으로 server - API문서를 작성해버림..

      > 이 때문에 API문서를 참조하는 데에 정말로 불편했다.
      > *대체 이 `request`는 어느 문서에 있는 걸까.. 뒤적뒤적*
      > router 들을 돌아다니다가 뭘 찾는지도 잊는 일들이 많았다.. 

   2. 모든 error상황을 미리 생각해두지 않았다.
      이 부분은 경험 부족에서 발생한 상황인 듯 하다.
      한가지 요청에 DB 접근이 힌 번 인 것 보단, 여러 번 인 것이 더 많은데,  이 때 발생할 수 있는 에러상황에서의 response를 생각해 두지 않았기에 **Client**와의 소통이 어려웠던것 같다 
      *(client를 하시는 대연님과 수지님은 다시 작성하는 것을 기다려 주셨지만.. 문서를 작성해놓고 무용지물인 상황을 맞이함.)*
      
      >    왠만한 CRUD코드를 작성 완료하고 API문서를 다시 수정하면서 *정말정말* 번거롭고 민폐였던 것 같다... 
      >    기획 때 부터 상세해 적어놓을걸!
   
3. **기본 router과 ** 에러 상황을 설정해줌!

   ````typescript
   api.use("", BasicRouter);
   
   api.use((req:Request, res:Response) => {
       res.status(404).send("Invalid address.Please check the address again");
   });
   
   api.use((err:Error, req:Request, res:Response, next:NextFunction) => {
       // eslint-disable-next-line no-console
       console.error(err.stack);
       res.status(500).send("Something broke!");
   });
   ````



