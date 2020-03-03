# OAuth2

## 1. 수업소개

OAuth는 3개의 참여자가 존재한다.

1. 우리의 서비스
2. User
3. (우리의 서비스가 연동하려고 하는 서비스) google, Facebook, Twitter

OAuth를 이용하면 훨씬 더 안전하게 우리의 서비스를 그들의 서비스와 연동 할 수 있다.
OAuth를 통해 그들의 서비스에 accessToken을 획득한 다음, accessToken을 통해서 그들의 서비스에 접근, 작업을 할 수 있게 되는 것이다.

**OAuth를 통해서 accessToken을 얻어 낼 수 있다.**

이러한 특징을 이용한다면, 회원의 아이디와 비밀번호를 가지고 있지 않아도 타 서비스로 로그인을 구현 할 수 있다.

## 2. 역할

앞서 설명했던 것의 용어 정리

1. Resource Owner (User)
2. Resource Server (그들의 서버 - 데이터를 가지고 있는 서버)
   Authorization Server ( 인증과 관련된 처리를 담당하는 서버, 공식 메뉴얼에서는 분리되어 있음.)
3. Client (우리의 서버)

## 3. 등록

클라이언트가 resource를 이용하기 위해서는 시전에 승인을 받아야 한다. 서비스마다 다르지만, 공통적으로 아래 요소를 받는다.

| 항목                     | 내용                    | 설명                                                         |
| ------------------------ | ----------------------- | ------------------------------------------------------------ |
| Client ID                | 1                       | 우리가 만들고 있는 application을 식별하는 ID<br />외부 노출되도 괜찮으나, secret은 금기. |
| Client Secret            | 2                       | id에 match되는 password                                      |
| Authorized redirect URIs | https://client/callback | resource server가 auth server가 권한을 부여하는 과정에서 auth code를 전달함.<br />그 때에 이 주소(클라이언트의 주소) 외에 다른곳에서 요청을 보내면 요청은 무시됨 |



## 4. Resource Owner의 승인

Client가 Server에 등록이 먼저 이루어 진 뒤, 만일 사용자(혹은 Resource owner) server의 권한을 필요로 하는 행위를 한다면 사용자에게 특정화면을 노출해야한다.
(예를들어, 페이스북으로 로그인하기 라던가..)
그렇다면, 그 화면(버튼)에는 

````
https://resource.server/?client_id=1&scope=B,C&redirect_uri=https://client/callback
````

이라는 url이 담겨져있다.

서버에서는 redirect 가 들어오면, client_id와 일치하는 redirect인지 확인하고,  일치하지 않는다면 거부를 한다.
일치한다면 scope에 해당하는것을 사용자에게 확인하는 메세지를 작성하여 owner에게 보여주게 된다. 

> ~~한것을 클라이언트가 요청하고있다. 허용할것이냐?

허용을 누르면, server에 전달이 되고, server의(service에서) userId가 전달되고, Server 가 그 값을 갖게 된다.

## 5. Resouce Server 의 승인

userId를 갖게된 ResouceServer은 바로 accessToken을 발급하지 않는다.

`authorization code`를 발급하여 resouce Owner에게 전달하게 된다.



