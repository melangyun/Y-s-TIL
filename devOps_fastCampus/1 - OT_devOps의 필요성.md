# DevOps의 필요성

- 2008년 애자일 컨퍼런스에서 앤드루 클레이 쉐이퍼와 패트릭 드부와가 
"애자일 인프라스트럭처"에 대해 논의하며 처음으로 사용
- 소통, 협업, 통합 및 자동화를 강조하는소프트웨어 개발 방법론
- 개발과 운영이 상호 의존적으로 대응해야 한다는 의미
    - sw제품, 서비스가 알맞은 시기에 출시하기 위해
- 개발과 운영 사이의 역할(어떻게 하면 더 효율적이고 빠르게 업무를 수행 할 수 있을 것인가?)

# 툴체인
- Jira
- Confluence
- Bitbucket
- Jenkins

# 업무환경(클라우드)
- Cloud Server (EC2, S3, RDS)
- Docker

# Jira & Confluence 에 대한 간략한 설명
- DevOps를 도입한다고 해서 꼭 모든 부서의 업무가 엄청 효율적으로 된다는 보장 이있는 것은 아니다.

<br>
그렇다면 왜 이런 협업도구를 사용해야 할까?
<br>

# 개발 프로세스
> 코드 -> 빌드 -> 테스트 -> 패키지 (java - war) -> 릴리즈 -> 모니터링

구성 - infra 구축
장애, 오류시에 복구에 대한 대응을 할 수 있다.

# Jira vs Confluence
Jira는 협업도구이다.<br>
Jira는 업무를 배정하고, 처리하고, 해당 업무에 대한 source를 볼 수 있다.<br>
Jira Confluence는 업무 자료를 정리하기에 매우 강력한 도구이다.<br>
slack같은 업무용 채팅들이 보급화 되어있지만, 업무에 대한 내용을 tracking 하기에는 번거롭다.
<br>
문자나 메일, 알람 등을 활용할 수 도 있다.

# Bitbucket, Jenkins
Bitbucket은 형상관리 툴, <br>
Jenkins는 Bitbucket으로 가져와 빌드하고 pipeLine을 통하여 배포 할 수 있다.