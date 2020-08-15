# AWS
클라우드 서버 구축 서비스
- 전통적 IDC (International Data Corporation)
- 점차 클라우드 서비스 중요도 증대

# Docker
오픈 소스 컨테이너 프로젝트로 만들어진 도커<br>
도커 없이도 서비스는 올릴 수는 있다. 도커에 패키징을 하게 된다면 소프트웨어를 제어 하는데에 용이해지게됨<br>
memory, io 제어, 접근권한 통제 가능<br>


# AWS의 장점과 단점

## 장점
- 탄력적인 웹 규모 컴퓨팅
    - 작은 규모로 부터 시작할 수 있고, 규모를 키워나가는데 적합하다.
    - 갑작스러운 트래픽이나 성장에 대응 할 수 있다.
- 다양한 Command(API)제공
    - 때에 따라 추가하고 붙이고 가능!(돈만 낸다면)
- 유연한 클라우드 호스팅 서비스
- 통합
    - storage, VPC, 등등
- 안정성
- 보안
    - (잘 알고 설정한다면..) (모르면 엄청난 청구 있을 수 있음)

## 단점
- 베어 메탈 성능을 원할 때
    - 베어 매탈 성능 : 고성능 물리서버, 
- 웹 페이지가 몇개 뿐일 때
- 플랫폼 보다는 솔루션에 적합
- 가격 ( 잘 사용하지 않는다면 비싸다 )

# AWS 의 종류
Server, storage, DataBase

## Server
- EC2(Elastic Compute Cloud)
    - 안전하고 크기 조절이 가능하다.
    - 개발자가 더 쉽게 웹 규모의 cloud computing 작업을 할 수 있게 되어있다.
    - auto scaring 자동 확장, 축소 가능
    - 완전 제어 가능,
    - 클리 제공, 다양한 Command API제공

- Lambda
    - 사용한 computing시간만큼만 요금이 부과되고, 사용되지 않을 때에는 요금이 부과되지 않음
    - 사실상 모든 유형의 back-end코드를 실행할 수 있다.
    - Lamda의 장점으로는 aws 서비스 및 쉬운 확장이 가능하다.
    - S3, dynamoDB 등 amazon API gateway를 통하여 custom API가능 
- VPC(Virtual Private Cloud)
    - 고객이 정의하는 가상 resource 에서 AWS를 시작 할 수 있도록 AWS cloud에 격리된 공간에서 시작 할 수 있다.
    - 가상 네트워킹 환경을 완벽하게 제어 할 수 있다.
    - IP V4, IP V6를 이용하여 제어 가능
    - 다중 연결 옵션을 선택할 수 있음
## Storage
- S3
    - S3를 통해 비용 최적화
    - 엑세스 제어 및 규정 준수 테이터 유연히 제공 가능
    - S3에 있는 DB에 대한 data분석 바로 실행 가능
    - 높은 안정성, 확장성
    - 데이터 -> aws region으로 자동 복제 가능 
- EBS(Elastic Block Store)
    - AWS Cloud에 EC2 Instance 에 사용할 영구 block storage block을 제공함
    - 가용 블록 내에 자동으로 복제되어 장애로부터 보호. 내구성
    - 지연시간이 짧음,안정적
    - 탄력적 운영 가능
    - 동적 변경 가능, 튜닝 가능
    - Amazon Cloud watch를 lamda와 함께 사용하면 자동으로 volume변경이 가능함
    - 등등
## DataBase
- RDS
    - 관리형 관계형 DB서비스
    - 사용의 편의성!
    - 튜닝도 가능
    - SSD 사용 ~!
    - 즉각적 확장가능
- DynamoDB
    - 빠르고 유연한 noSQL DB Service
    - 빠름!
    - 문서 저장, 쿼리 저장 가능
- RedShift
    - 속도가 빠른 완전 관리형 DB
    - 간편, 비용이 효율적
    - 정교한 쿼리, 최적화, 대량 병렬, 복잡한 분석 쿼리 가능
    - DW 등, sql 작업을 병렬처리
- AuroraDB
    - 고성능 사용 db
    - mysql, postgres, 
    - mysql 보다 5배 뛰어남, 가용성, 안정성 좋음
    - 1/10가격으로 제공
    - 모니터링, db,복제, enterprise급 서비스 제공
    - 즉각적 computing 기능 가능
    - 읽기 전용 복제 가능


## Management - Cloud Watch
자동 대응 가능<br>
EC2 instance, RDS DB Instance 등, <br>
EC2 사용시 추가비용 없이 monitoring 가능<br>
비용 추가시 세부적으로 가능

## Analysis - Kinesis
실시간 데이터 수집, 분석<br>
완전 관리형, 인프라 통합 관리, 

# Docker

## 장점
> 실행 시점에 상관 없이 구성 시점을 고를 수 있음

- 버젼 관리 차원에서 동시에 배포가 가능 (이미지 화)
- 눈송이 서버 : 서버가 많아질 때 각 서버별로 버젼이 상이함 -> 이미지를 늘 똑같이 컨테이너에 배포하게 되면 해당 문제는 많이 줄어들게 된다. 

> 개발 프로그램 설치와 삭제가 용이

Java, mysql, oracle, elk, nginx 등 서버 프로그램 설치와 삭제가 용이 

> 운영체제 도커 실행 소스 일관성, 유연성

- 초기 인프라 환경 설정은 복잡하고 어려우나, 쉽고 일관성이 있게 만들어줌

> 이미지 용량이 크게 줄어듬
- 도커는 리눅스 컨테이너를 사용

> 여러군데 배포할 수 있는 확장성
- Github와 비슷한 느낌으로 push/pull 용이