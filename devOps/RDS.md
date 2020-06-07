# Database Server
- 데이터베이스의 사용량이 많은 경우 하나의 데이터베이스로 모두 처리하는데 부담이 될 수 있다. 따라서 Master, Slave 등의 관계로 같은 데이터를 갖고 잇는 데이터 베이스를 여러개 생성하여 요청을 분산 처리한다. 보통 Master는 write용, slave는 read 용으로 사용한다.