# 20.02.01(토) - 20.02.02(일) 주말 DevLog - server project setting

1. ESLint 설정

   - 성현님과 함께 ESLint설정을 하였다.
     기존에 ESLint extention을 설치해 두었지만, (주도적으로)사용을 하지 않았어서 한참 걸린것같다.
   - 기본 수정 tool설정과 Lint설정 후 성공적으로 적용하는데 까지 2~3시간은 거뜬히 걸린것같다....
   - 내 프로젝트에서 적용되기 시작하니까 성현님의 local에서 적용되지 않아서... 한참 헤맨것같당
     몇시간 후에 컴퓨터 자체를 껐다가 켜니 적용되었다고 한다. 무언가 vsCode에서의 오류가 아니였을까?
   - **airbnb**설정을 사용하게 되었다.

2. Server 및 DB설정, TypeORM학습 

   - 성현님이 Server를 띄우는 동안 나는 TypeORM학습 후 알려주기로 하였다.

   - Sample로 코드를 작성해보았고, 공식문서도 나름대로 꼼꼼히 읽으려고 노력했다.
**[typeORM Cheatsheet](https://cheatsheets.joshuatz.com/cheatsheets/typeorm/)**
     
     | 참조사이트                                                   | 설명                                                         |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | [stackoverflow - How to create this ViewEntity with TypeORM?](https://stackoverflow.com/questions/59448115/how-to-create-this-viewentity-with-typeorm) | TypeORM에서 view생성                                         |
     | [typeORM_github : How to query a view instead of a table?](https://github.com/typeorm/typeorm/issues/1024) | TypeORM에서 view생성                                         |
     | [typeORM guide - typeorm.io](https://typeorm.io/#/)| typeORM 튜토리얼    |
     | [typeORM github](https://github.com/typeorm/typeorm/blob/master/docs/entities.md) | typeORM 깃허브                                               |
     | [typeORM_github-Point has different type for get](https://github.com/typeorm/typeorm/issues/2896) | typeORM - Point자료형 사용에 대한 issue                      |
     | [Mysql_point사이의 거리계산](https://purumae.tistory.com/198) | mysql point사용 및 거리 계산 예제 blog                       |
     | [Difference between VARCHAR and TEXT in mysql](https://stackoverflow.com/questions/25300821/difference-between-varchar-and-text-in-mysql) | typeORM **varchar vs text**<br />varchar는 크기 조절이 되나, text type은 max size로 fix된다. |
     | [typeORM_delightful_stdio](https://typeorm.delightful.studio/modules/_driver_types_columntypes_.html) | typeORM Column type 종류                                     |
     | [char/varchar와 nchar/nvarchar 비교](http://blog.naver.com/PostView.nhn?blogId=newcomsa&logNo=30081390512) | varchar vs nvarchar                                          |
     | [MYSQL DATETIME VS TIMESTAMP 차이](http://blog.daum.net/_blog/BlogTypeView.do?blogid=03aaf&articleno=12379936&_bloghome_menu=recenttext) | mysql DateTime vs TimeStamp                                  |
     | [TypeOrm의 ManyToMany 와 JoinTable 사용하기](https://medium.com/@hckcksrl/typeorm의-manytomany-와-jointable-사용하기-5764e5e51d9) | JoinTable사용을 위해 참조한 blog설명                         |
     
        
     
   - Type ORM을 작성하다보니 `experimentalDecorators`를 조정하라는 eslint warning이 생성되는데, `tsconfig.json`파일에서 아래 옵션을 적용하여도 warning이 해소되지않는다..! 왜그런지 전혀 모르겠다 ㅠㅠ..
   
     ````json
     {
         "compilerOptions": {
             "experimentalDecorators": true,
             "allowJs": true
         }
     }
     ````
   
   - Join table을 작성해 보았다. (Cat테이블과, Tag테이블 사이의 Join table!)
     **Tag.ts**
   
     ````typescript
     import {
         Entity, BaseEntity, PrimaryGeneratedColumn, Column, ManyToMany,
     } from "typeorm";
     
     import Cat from "./Cat";
     
     @Entity({ name: "tag" })
     export default class Tag extends BaseEntity {
           @PrimaryGeneratedColumn()
           id: number;
     
           @Column()
           content:string;
     
           @CreateDateColumn()
           createAt: Date;
     
           @UpdateDateColumn()
           updateAt: Date;
     
           @ManyToMany((type) => Cat, (cat) => cat.id, { cascade: true })
           cats: Cat[];
     }
     
     ````
   
     **Cat.ts**
   
     ````typescript
     import {
         Entity, BaseEntity, PrimaryGeneratedColumn, Column, CreateDateColumn, UpdateDateColumn, ManyToMany,
     } from "typeorm";
     import Tag from "./Tag";
     
     @Entity({ name: "cat" })
     export default class Cat extends BaseEntity {
         @PrimaryGeneratedColumn()
         id:number;
     
         @Column({ type: "nvarchar", comment: "a brief explanation of about 200 characters based on uniCode." })
         description:string;
     
         @Column({ type: "point", nullable: "false" })
         location:string;
     
         @Column({ type: "varchar", nullable: "false" })
         nickname:string;
     
         @Column({ type: "varchar", nullable: "false", length: 100 })
         cut:string;
     
         @Column({ type: "varchar", nullable: "false", length: 100 })
         rainbow:string;
     
         @Column({ type: "varchar", nullable: "true" })
         species:string;
     
         @Column({ type: "varchar", nullable: "true" })
         today:string;
     
         @Column({
             type: "timestamp", name: "today_time", nullable: "true", comment: "Time when \"today\"column updated",
         })
         todayTime:Date;
     
         @CreateDateColumn()
         createAt: Date;
     
         @UpdateDateColumn()
         updateAt: Date;
     
         @ManyToMany((type) => Tag, (tag) => tag.id, { cascade: true })
         tags:Tag[];
     }
     
     
     ````
   
   - DB Connection을 위해 어제 성현님이 띄워놓은 server setting을 보다 보니 조금 고치고 싶은 부분들이 있어 고치기 시작했다.
   
   - Cors를 실수로 devDependencies로 설정해 놓아 삭제 후 재설치를 하였음
   
      ````bash
     $ npm uninstall cors
     #devDependencies 와 Dependencies의 module를 모두 지움
     $ npm install cors --save
     ````
     
   - router 전체적인 파일구조를 설정하였음
   
   - `npm start`를 할때 `package.json`에서 build를 설정해놓지 않았기때문에 그동안의 수정사항이 변경되지 않았음.
   
     + build 되는 `dist`파일들 `.gitignore`에 추가
       **이미 git에 등록되어있는 파일들을 제거하기 위해 git ignore을 재적용하였다!**
   
       ````bash
       $ git rm -r --cached .
       $ git add .
       $ git commit -m "Apply .gitignore"
       $ git push [options]
       ````
   
       
   
   - 처음으로 `git conflict`를 해결해 보았다! -> 깃허브에서..!
   
   - `ts`빌드 재설정 이후 `npm start`로 아래 DB test코드를 돌려보았을때 에러가 난다..왜그럴까?
   
     ````typescript
     data
         .getConnection()
         .then(async (connection:typeorm.Connection) => {
             const catRepository:typeorm.Repository<Cat> = connection.getRepository(Cat);
             const tagRepository:typeorm.Repository<Tag> = connection.getRepository(Tag);
     
             const cat = new Cat();
             cat.location = "(0,0)";
             cat.nickname = "운영냥";
             const testCat = await catRepository.save(cat);
     
             const tag = new Tag();
             tag.content = "권위적임";
             const testTag = await tagRepository.save(tag);
     
             console.log(testCat);
             console.log(testTag);
             // return;
         })
         .catch((err) => conso
     ````
   
     **error log 를 보았을 때, test코드가 아니라, entity 작성 코드에서 무언가 문제가 있는것같다.**
     아무튼, 그동안 무언가 답답했던 부분이 package.json을 꼼꼼히 보지 않아서였다니, 앞으로는 빼먹는 부분이 적어지도록 해야겠다...
   
     오늘(일) 하루 학습 및 에러 내용 성현님과 잠시 후 공유하기로 하였다.
   
   - 성현님과 함께 에러를 구글링해서 잡았다! 원래 Connection 때문의 error였는데, 테이블 생성은 정상적으로 이루어지고, Join Table또한 한가지 문법적으로 놓친것을 고쳤다.
      또, 문법적으로 틀린것들 또한, 성현님과 함께보고 고쳤따..! 왜 모든걸 string으로 작성햇떤거지..
   
   - Cat.ts 수정
   
      ````typescript
      /* eslint-disable import/no-unresolved */
      /* eslint-disable import/extensions */
      import {
          Entity, BaseEntity, PrimaryGeneratedColumn, Column, CreateDateColumn, UpdateDateColumn, ManyToMany, JoinTable,
      } from "typeorm";
      import Tag from "./Tag";
      
      @Entity({ name: "cat" })
      export default class Cat extends BaseEntity {
          @PrimaryGeneratedColumn()
          id! :number;
      
          @Column({ type: "nvarchar", nullable: true, comment: "a brief explanation of about 200 characters based on uniCode." })
          description! :string;
      
          @Column({ type: "point", nullable: false })
          location! :string;
      
          @Column({ type: "varchar", nullable: false })
          nickname! :string;
      
          @Column({ type: "varchar", nullable: false, length: 10 })
          cut! :string;
      
          @Column({ type: "varchar", nullable: false, length: 100 })
          rainbow! :string;
      
          @Column({ type: "varchar", nullable: true })
          species! :string;
      
          @Column({ type: "varchar", nullable: true })
          today! :string;
      
          @Column({
              type: "timestamp", name: "today_time", nullable: true,
          })
          todayTime! :Date;
      
          @CreateDateColumn()
          createAt! : Date;
      
          @UpdateDateColumn()
          updateAt! : Date;
      
          @ManyToMany((type) => Tag, (tag) => tag.id, { cascade: true })
          @JoinTable()
          tags! :Tag[];
      }
      
      ````
   
      `! : ` 는 초기 값을 보장할 수 없다는 것이라고 한다.
      또, comment 의 ''또한 에러가 났고, default option또한 그로인해 에러가 났기때문에 임시방편적으로 제거했다.
      사용하는 방향으로 가고싶은데, 에러가 쉬이 잡히지 않으면 사용하지 않을 수 도 있을것같다. typeORM으로 default를 설정한다고 해도 이점이 크지 않을것같다는 생각과 성현님 의견이다..!
   
      ````mysql
      MariaDB [cats]> show tables;
      +----------------+
      | Tables_in_cats |
      +----------------+
      | cat            |
      | cat_tags_tag   |
      | tag            |
      +----------------+
      3 rows in set (0.001 sec)
      
      MariaDB [cats]> describe cat;
      +-------------+--------------+------+-----+----------------------+----------------+
      | Field       | Type         | Null | Key | Default              | Extra          |
      +-------------+--------------+------+-----+----------------------+----------------+
      | id          | int(11)      | NO   | PRI | NULL                 | auto_increment |
      | description | varchar(255) | YES  |     | NULL                 |                |
      | location    | point        | NO   |     | NULL                 |                |
      | nickname    | varchar(255) | NO   |     | NULL                 |                |
      | cut         | varchar(10)  | NO   |     | NULL                 |                |
      | rainbow     | varchar(100) | NO   |     | NULL                 |                |
      | species     | varchar(255) | YES  |     | NULL                 |                |
      | today       | varchar(255) | YES  |     | NULL                 |                |
      | today_time  | timestamp    | YES  |     | NULL                 |                |
      | createAt    | datetime(6)  | NO   |     | current_timestamp(6) |                |
      | updateAt    | datetime(6)  | NO   |     | current_timestamp(6) |                |
      +-------------+--------------+------+-----+----------------------+----------------+
      11 rows in set (0.002 sec)
      
      MariaDB [cats]> describe cat_tags_tag;
      +-------+---------+------+-----+---------+-------+
      | Field | Type    | Null | Key | Default | Extra |
      +-------+---------+------+-----+---------+-------+
      | catId | int(11) | NO   | PRI | NULL    |       |
      | tagId | int(11) | NO   | PRI | NULL    |       |
      +-------+---------+------+-----+---------+-------+
      2 rows in set (0.001 sec)
      
      MariaDB [cats]> describe tag;
      +----------+--------------+------+-----+----------------------+----------------+
      | Field    | Type         | Null | Key | Default              | Extra          |
      +----------+--------------+------+-----+----------------------+----------------+
      | id       | int(11)      | NO   | PRI | NULL                 | auto_increment |
      | content  | varchar(255) | NO   |     | NULL                 |                |
      | createAt | datetime(6)  | NO   |     | current_timestamp(6) |                |
      | updateAt | datetime(6)  | NO   |     | current_timestamp(6) |                |
      +----------+--------------+------+-----+----------------------+----------------+
      4 rows in set (0.001 sec)
      ````
   
      

