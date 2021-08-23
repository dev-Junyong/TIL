#homework
#1
# class Circle:
#     pi = 3.14
#     x = 0
#     y = 0
#     r = 0
    
#     def __init__(self, r, x, y):
#         self.r = r
#         self.x = x
#         self.y = y
        
#     def area(self):
#         return self.pi * self.r * self.r
    
#     def circumference(self):
#         return 2 * self.pi * self.r
    
#     def center(self):
#         return (self.x, self.y)
    
# c1 = Circle(3,2,4)
# c1.area()
# c1.circumference()
#c1.r = 3
# c1.x = 2
# c1.y = 4


#2
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def walk(self):
#         print(f'{self.name}! 걷는다!')

#     def eat(self):
#         print(f'{self.name}! 먹는다!')

# # 명시적 init을 해도 상관없음 (원래 답처럼)
# class Dog(Animal):
#     def walk(self):
#         print(f'{self.name}! 달린다')

#     def bark(self):
#         print(f'{self.name}! 짖는다')

# class Bird(Animal):   
#     def fly(self):
#         print(f'{self.name}! 푸드덕')


# dog = Dog('멍멍이')
# dog.walk()
# dog.bark()

# bird = Bird('구구')
# bird.walk()
# bird.eat()
# bird.fly()




#3
'''
ZeroDivisionError
: 어떠한 수를 0으로 나눌 때 발생하는 에러
NameError
: 사용하려는 변수 혹은 함수 등이 없을 경우, 정의되지 않은 무언가를 사용하려하는 경우
TypeError
: 자료형이 맞지 않거나 함수 호출 문법을 지키지 않은 경우, 잘못된 자료형으로 접근 or 제어하려고 할때
IndexError
: 리스트의 인덱스 범위를 벗어나는 경우, 인덱스 범위를 벗어나서 조작하려고 할때(리스트에서 주로 발생)
KeyError
: 딕셔너리 안에 해당하는 key가 없는 경우 발생, 딕셔너리에서 주로/없는 키를 호출하려할때
ModuleNotFoundError
: 검색한 모듈을 찾지 못하는 경우 발생, 패키지/모듈을 찾을 수 없을때
ImportError
: 경로 위치에 대한 오류가 있는 경우 발생, 패키지/모듈은 존재// 가져오려는 것(변수, 함수, 클래스)이 없을 때
'''



#workshop
class Point:
    def __init__(self, x: int, y: int) -> None:  # 이런식으로도 표현 가능, 입력시 형식이 틀려도 오류 안남(타입힌트)
        self.x = x
        self.y = y
    

class Rectangle:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2
        self.get_wid_leng()
    
    #가로, 세로 길이 구하는 메서드
    def get_wid_leng(self):
        self.width = abs(self.p1.x - self.p2.x)
        self.length = abs(self.p1.y - self.p2.y)


    def get_area(self) -> int:
        return self.width * self.length
    
    def get_perimeter(self) -> int:
        return (self.width + self.length) * 2

    def is_square(self):
        return self.width == self.length


p1 = Point(1,3)
p2 = Point(3,1)
r1 = Rectangle(p1,p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3,7)
p4 = Point(6,4)
r2 = Rectangle(p3,p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())



