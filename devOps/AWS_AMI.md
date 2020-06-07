# AWS AMI 생성
EC2 인스턴스를 추가할 때마다 새롭게 설정(Nginx 설치, 설정 파일 변경, 실행) 해야 할까?

AMI를 스냅샷을 찍고 CD처럼 구울 수 있다. 바로 AMI(Amazon Machine Image)!

**AMI를 기준으로 자동으로 EC2 인스턴스가 생성될 때 Nginx 프로세스를 자동으로 실행하기 위해 systemctl애 nginx 실행 등록**

```bash
$ sudo su
$ systemctl enable nginx
```

1. AWS에서 인스턴스 -> 이미지 생성
    - 기존 생성된 EC2 인스턴스의 설정을 기반으로 AMI 생성


# Auto scaling group

- 특정 조건에 해당되면 자동으로 EC2 생성, 운영해준다.
    - **Scale out 이 자동화됨**