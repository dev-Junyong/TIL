#homework
# 1번
# 기본적으로 정의되어 있는 클래스
from _typeshed import Self


int
list
dict
set
bool
str
complex
range
map
zip


# 2번
#매직메서드
# __init__
# 생성자, 인스턴스가 생성될때

# __del__
# 인스턴스가 삭제될때

# __str__
# 문자열, print()할 때 보여지는 (인스턴스 값) 문자열 반환 / 사용자도 볼 수 있음
# 외부노출

# __repr__
# 문자열, 인스턴스의 정보에 대한 값을 반환 / 개발자가 개발할때 개발자가 확인하고 싶다할때
# 내부용



# 3번
# String: upper, lower, title, split, join, strip
# list: count, pop, reverse, index, append, extend, sort,
# dictionary: update, values, keys, items, get,



# 4번
# (a): fibo
# (b): fibo_recursion
# (c): recursion



#workshop
# 1번
# (1) 페이커 설치
# (2) TLI 환경, 터미널

# 2번
# 1. faker라는 패키지에서 Faker라는 클래스를 불러와 사용준비를 하기 위한 코드이다.
# 2. Faker는 클래스이고, fake는 인스턴스이다
# 3. name()은 fake의 인스턴스 메서드이다


# 3번
# (a): init
# (b): self
# (c): locale = 'en_US' # 변수명은 아무거나, 매개변수이기 때문에 그냥 자기가 지정, 아무거나 상관없음
# 'en_US' -> 얘는 영문이 기본 설정이라 필요

# 1. 생성자. => 인스턴스 생성할때 실행
# 2. 인스턴스 메서드 => 첫번째 인자 self
# 3. 인스턴스가 생성될 때, 인자가 있으면 그 값은 생성자로 들어간다



# 4번
#1. 이도윤
#2. 이지후
#seed() -> 클래스 메서드
# name() -> 인스턴스 메서드



#1. 이도윤
#2. 랜덤 -> fake2는 영향을 받지 않음
# seed() -> 클래스메서드로 클래스 변수가 변경되어 모든 인스턴스에 적용됨 (전체 설정)
# seed_instance() -> 인스턴스메서드이고, 인스턴스 변수가 변경이 되고 해당 인스턴스에 적용됨 (일부 설정)








