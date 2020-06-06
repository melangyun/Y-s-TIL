# EC2란
- AWS에서 제공하는 가상서버 (Virtual Machine, VM)
- Amazon Linux, Cent Os, Ubuntu, Windows등 다영한 OS 제공
- 원하는 사양을 관리자가 직접 선택할 수 있음
- 필요할 때마다 사용/ 중지가 가능

## Virtual Machine
가상머신은 "실제 컴퓨터의 효율적이고 고립된 복제물" 로 정의한다.
현재는 `실제 하드웨어와 직접적인 통신이 없는 가상 컴퓨터` 를 가르킨다.

[위키백과](https://ko.wikipedia.org/wiki/가상_머신)

시스템 가상 머신들은 실제 기계의 대체제를 제공하고, 완전한 운영체걔ㅖ 실행을 위해 요구되는 기능성의 수준을 제공힌다.

## Amazon Linux2
- AWS에서 제공하는 차세대 Linux 운영 체제
- Amazon Linux Extras 레포지토리를 통해 최신 소프트웨어 패키지 제공
- Container 환경에 최적화된 OS

## Amazon 머신 이미지
- 서버 인스턴스의 기반이 되는 이미지
- 윈도우 CD, iso와 같은 개념
- Amazon에서 제공하는 빅데이터, 웹서비스 등 각 기능 별로 빌드한 이미지를 사용하거나 다른 사람이 공유하는 이미지도 사용 가능


## SSH
- SSH(Secure shell)은 다른 컴퓨터에 접속하거나 원격 시스템에서 명령을 실행 할 수 있는 클라이언트/ 프로토콜을 의미
- 대부분의 리눅스 배포판에선 기본적으로 설치되어이있음
- 22번 포트 사용
- `-i`옵션으로 비밀번호가 아닌 SSH key로 접속

## SSH Key
- 비밀번호 보다 높은 수준의 보안을 필요 할 때 사용
- 서버에 저장된 *Public key*와 사용자의 *Private Key*를 비교하여 확인 됬을 때만 접속을 허용

## Web Server
- HTTP 요청을 받고 응답하는 역할을 함
- HTTP transaction을 처리하고, 정적인 파일 (static file - HTML, CSS, Image 등)을 요청한 대상에게 보내준다.
- Application logic을 직접 처리할 수 없어 WAS(Web application server)와 같이 사용한다.
- 대표적으로 Apache, NginX와 같은 제품이 있다.

# DNS
- 도메인 네임 서비스
- 모든 디바이스(인터넷 연결이 가능한)는 IP(192.xx.xx)로 통신한다.
- IP를 외우기엔 번거로워 IP와 URL을 매핑하여 전화번호부 같은 역할을 한다.

# Port
- TCP/IP로 접속 시 마지막 종단점
- 클라이언트 실행 시 동적으로 Port 번호가 부여됨
- 해당 인스턴스에서 실행되는 클라이언트의 구분을 위해 사용
- 일반적으로 SSH(22번), HTTP(80번), WAS(8080번)을 부여
- 도메인(URL)로 접속 시 기본적으로 80번 포트를 사용(생략 가능)

> Amazon Linux2 를 기반으로 하는 AWS AMI를 활용하여 EC2를 생성하고 SSH클라이언트로 접속하여 해당 VM에 웹서버 (NginX)를 설치 후 웹 브라우저를 통해 DNS:80포트에서 확인하였음

```bash
# sudo : 현재 계정에서 다른 계정의 권한만 빌림
# su : 다른 계정으로 전환
# sudo su로 작업하면 소유자가 root가 된다.
sudo su
```