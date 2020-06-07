# 많이 사용하는 제품들 - HTTP Web server
- 서비스
    - NginX
    - Apache
    - IIS (Windows 서버)

- 차이점
    - 제공되는 OS
    - 성능
    - 연동되는 Application Server

# 많이 사용하는 제품들 - WAS
- 서비스
    - Java
        - Tomcat, JBoss, Jetty
    - Node.js
        - PM2(Process manager)
        - impress
    - Python(WSGI)
        - GUnicorn, uWSGI
    - Ruby
        - Phusion Passenger, Puma

- 차이점
    - 지원하는 언어

# 많이 사용하는 제품들 - Cache
- 서비스
    - in-memory - 데이터를 메모리에 저장, Read/Write
    - Memcached
    - Redis
- 차이점
    - 제공되는 기능
        - key/value store을 넘어서 db, message broker 등
        - 제공되는 데이터 구조

# 많이 사용하는 제품들 - Monitoring
- 서비스
    - AWS Cloudwatch
    - NHN Pinpoint
        - Opensource APM(Application performance monitoring)
    - ELK - Elastic search, Logstash, Kibana(https://www.elastic.co/kr/elk- stack)
        - log monitoring
    - Grafana
        - Metric(cpu, ram, disk, etc...) monitoring

# 많이 사용하는 제품들 - CI/CD
- 서비스
    - Jenkins CI
    - Circle CI
    - AWS Codepipeline