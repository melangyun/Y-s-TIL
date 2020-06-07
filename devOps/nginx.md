````nginx.conf
    keepalive_timeout   65;
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        root         /usr/share/nginx/html/Fastcampus-web-deploy;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
        }
        # Nginx에 요청된 URL별 특정 위치에 적용할 설정 그룹에 대한 정의 내용
        # 여러 URL을 처리하기 위해 정규표현식을 사용하는 경우가 일반적임

        location ~* /(album|signin) {
            # nginx가 처리하는 URL이 album혹은 signin에 매칭되는지 확인
            # 해당 URL이 매칭된다면 Nginx root 디렉토리를 해당 블럭에 적힌 디렉토리로 변경
          root /usr/share/nginx/html/Fastcampus-web-deploy/page;
        }

        # reverse proxy
        # 들어온 요청을 다른 웹 서버 or WAS로 전달
        # DB서버와 연결되 있는 WAS의 ip와 포트 번호를 감출 수 있음 (보안)
        location /api {
            proxy_pass ec2-15-165-76-146.ap-northeast-2.compute.amazonaws.com:8080
        }

        error_page 404 /404.html;
            location = /40x.html {
        }
 
````
위 설정 외에도 
- worker_process auth(or number) :
    - 몇개의 thread를 사용할 것인지 정의, CPU core 수를 넣어주면 된다.
    - auto로 설정하면 해당 머신의 CPU core 수 만큼 자동으로 설정된다.

- worker_connections 1024:
    - worker thread 당 최대 몇개의 connection을 처리할 것인지 정의
    - 최재 처리량 = worker_processes * worker_connections

- reverse proxy, Load balancer, web cache 서버 등 설정에 다라 다양하게 사용 가능