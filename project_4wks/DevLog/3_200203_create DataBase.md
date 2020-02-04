# 3_200203_create DataBase & Router

1. DB entity 작성을 완료하였다.

   - default  value를 설정하고싶었는데, string 값에 대한 defualt 설정에서 계속해서 에러가 나서 결국에는 typeORM 초기값으로 설정을 해주었다. 이것 저것 계속해서 구글링 해보았는데, 에러가 나지 않는 string default 값을 설정하는 법은 결국 찾지 못했다.

   - typeORM 에서 지원하는 column-type 에서 `simple-json`이라는 것이 있는데, 이를 사용하면 Insert시 자동으로 `ojbect`를 `string`형으로 변환아여 넣어준다. 하지만 DB에서의 data-type이 `text`로 설정되어 무분별한 사용을 지양해야 할것이다. 
     이 설명대로 작성한 코드는 아래와 같다.

     ````typescript
     @Column({
         type: "simple-json", nullable: false,
     })
     cut :{Y:number, N:number, unknown:number} = { Y: 0, N: 0, unknown: 0 };
     ````

   - `@ManyToMany`를 사용하면 연결된 table의 key가 자동으로 생성되지만, **pk외에 다른 column**을 추가하고싶다면 새로이 table을 형성하여 각각  `@oneToMany`, `@manyToOne`관계를 설정해주어야했다.
     또, `@ManyToMany`는 연결된 두개의 table중 하나에만 설정해주면된다.

   - MariaDB에서 한글 인코딩문제

     - `ormconfig.json`에서 계속해서 `chrset='utf8'`의 형식으로 계속해서 시도했으나, 한글인코딩에 계속하여 실패하였다. 이것 저것 시도해보다가 성현님이 db를 create할 때부터 Default encoding 형식을 지정해주면 해결되는것을 발견하였다.

       ````mysql
       CREATE DATABASE cats CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
       ````

   - location 항목의 point로 하는 방식(모듈필요 *wkx*)또한 성현님이 학습하여 공유하였고, db에 ponit형식으로 성공적으로 Insert되었다. 

     ````javascript
     const venue = new wkx.Point(1, 2).toWkt();
     cat.location = venue;
     ````

     

2. git 과 `ormconfig.json`과의 문제가 해결됨
   git pull을 받으면 날라가던

   - 이유는 모르겠다... 아무튼 `process.env~`변수를 사용하기 위한 세팅도 성현님과 함께 진행하였다.
   - 또한 **.env**설정을 하여 `git ignore` 설정까지 완료하였다.
   - 

3. Router filetree와 request들을 작성하였고, **API문서와** 싱크를 맞추었다.( `requset`와 `reponse`)를 모두 꼼꼼히 정리하여 협업하기 편리한 형태로 정리한것같다.



백지장도 맡들만 낫다고(?) 확실히 혼자서는 계속해서 헤매는 문제들이 성현(구글링의 신)님과 함께하면 금방금방해결하는것같다.
다만 문서 작성과 디비의 디테일한부분들 등을 신경쓰느라 코딩량은 아직까지 많지는 않지만 이제 거의 세팅이 끝났으니 코딩을 시작하면 수월히 진행될것이라 생각한다.

