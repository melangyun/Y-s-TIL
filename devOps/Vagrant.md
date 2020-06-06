# Vagrant
> 베이그런트 (Vagrant)는 포터블 가상화 소프트웨어 개발환경(개발 생산성 증가를 위해 가상화의 소프트웨어 구성 관리의 단순화를 시도하는 비추얼 박스, 하이퍼-V, 도커 컨테이너, VM웨어, AWS)의 생성 및 요지보수를 위한 오픈 소스 소프트웨어 제품의 하나이다. 

```bash
vagrant init
```
을 하면 Vagrant file이 생성된다.

참조 : (Vagrantfile에 대해서..)[https://m.blog.naver.com/PostView.nhn?blogId=sory1008&logNo=220755332201&proxyReferer=https:%2F%2Fwww.google.com%2F]

# Vagrantfile
![Vagrantfile](https://m.blog.naver.com/PostView.nhn?blogId=sory1008&logNo=220755332201&proxyReferer=https:%2F%2Fwww.google.com%2F#)

VagrantFile은 VM 환경설정 파일이다.
Vagrantfile의 주 목적은 프로젝트에 할당된 machine의 타입, machine 을 provision(공급)하고 설정하는 방법을 표현하는 것이다.
Vagrant 가 지원되는 플랫폼이라면, 어디든 옮겨서 사용할 수 있도록 되어 있다.
Vatrantfile의 구문은 Ruby로 되어 있지만 그렇다고 파일을 수정하기 위해서 ruby를 배워야 하는 것은 아니다.

## Lookup Path
vagrant 명령어를 날리면 현재 폴더에서 먼저 Vagrantfile을 찾으려고 하고, 찾지 못하면 점점 상위 폴더로 옮기면서 찾으려고 시도할 것이다.

## Load ordered and merging
Vagrantfiles 을 로드하는 방법은 반드시 이해하여야 한다.
Vagrant는 실제로 여러개의 Vagrantfiles를 로드하면서 세팅들을 병합한다.
즉 동일한 설정들이 여러 파일에 걸쳐서 있었다면 override 된다는 것을 의미한다.
만약 Vagrantfile이 검색이 안되었을 때 아래와 같은 절차를 진행한다.
1. box에 패키징 되어있는 VagrantFile
2. Vagant home 디렉토리(default)에 있는 Vagrantfile
3. project 디렉토리에 있는 Vagrantfile
4. Multi-machine overrides if any.
5. Provider-specific overrides, if any.

각 단계를 거치면서 기존 값들과 병합되면서 기존 값들을 덮어써 버린다.

## Machine Settings
Config namesapce: config.vm
아래와 같은 설정들이 있다.

https://www.vagrantup.com/docs/vagrantfile/machine_settings.html

config.vm.boot_timeout 
config.vm.box 
config.vm.box_check_update 
config.vm.box_url 
config.vm.box_version 
config.vm.communicator 
config.vm.graceful_halt_timeout 
config.vm.guest 
config.vm.hostname 
config.vm.network 
config.vm.post_up_message 
config.vm.provider 
config.vm.provision 
config.vm.synced_folder 
config.vm.usable_port_range

https://www.vagrantup.com/docs/vagrantfile/

# Vagrant 로 Ubuntu ubuntu vm 환경 구성
https://anewhope.tistory.com/entry/vagant-로-로컬-테스트-환경을-만들어-보자

- vagrant init [ubuntu/trusty64] 초기 템플릿 구성
    - 이렇게 되면 ubuntu/trusty64가 config.vm.box 에 들어간다.
- vagrant up으로 실제 vm 생성
- vagrant ssh로 생성된 vm 생성

