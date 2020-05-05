# 루비는 module을 분리 시킬수도, 그렇지 않을 수도 있다.
require_relative "./egoing"
require_relative "k8805"


puts(Egoing.a())
puts(K880.a())