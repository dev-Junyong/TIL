# #Q1
# import random

# def game(): 
#     a=input("가위 바위 보! : ")
#     b=random.randrange(0,3) # 0: 가위 1: 바위 2:보
#     if a=='가위':
#         a=0
#         if b==0:
#             print("다시 한번")
#         elif b==1:
#             print("컴퓨터 승리")
#         elif b==2:
#             print("승리")
#     elif a=='바위':
#         a=1
#         if b==0:
#             print("승리")
#         elif b==1:
#             print("다시 한번")
#         elif b==2:
#             print("컴퓨터 승리")
#     elif a=='보':
#         a=2
#         if b==0:
#             print("컴퓨터 승리")
#         elif b==1:
#             print("승리")
#         elif b==2:
#             print("다시 한번")

# game()

# #Q2
# def yearly_payment(m_payment):
#   yearly_before = int(m_payment)*12
#   if yearly_before <= 1200 :
#     print(1)
#     yearly_after = int(yearly_before * 0.94)
#   elif yearly_before <= 4600 :
#     print(2)
#     yearly_after = int(yearly_before * 0.85)
#   elif yearly_before <= 8800 :
#     print(3)
#     yearly_after = int(yearly_before * 0.76)
#   elif yearly_before <= 15000 :
#     print(4)
#     yearly_after = int(yearly_before * 0.65) 
#   elif yearly_before <= 30000 :
#     print(5)
#     yearly_after = int(yearly_before * 0.62)
#   elif yearly_before <= 50000 :
#     print(6)
#     yearly_after = int(yearly_before * 0.60)
#   else :
#     yearly_after = int(yearly_before * 0.58)
#   print("세전 연봉: "+ str(yearly_before) + "만원")
#   print("세후 연봉: "+ str(yearly_after) + "만원")
# monthly_payment = input("월급을 입력하세요")
# yearly_payment(monthly_payment)


# #Q3
# name_list = input("학생 이름 입력: ")
# score_list = int(input("학생 점수를 입력: "))

# def grade(score):
#     if score >= 95:
#         return 'A+'
#     elif score >= 90:
#         return 'A'
#     elif score >= 85:
#         return 'B+'
#     elif score >= 80:
#         return 'B'
#     elif score >= 75:
#         return 'C+'
#     elif score >= 70:
#         return 'C'
#     elif score >= 65:
#         return 'D+'
#     elif score >= 60:
#         return 'D'
#     else:
#         return 'F'

# print(f'학생 이름: {name_list}')
# print(f'점수: {score_list}점')
# print('학점: ', grade(score_list))



# # Q4
# table = {
#     0:{1:0, 2:0}, 1:{1:450, 2:450}, 
#     2:{1:720, 2:1000}, 3:{1:1200, 2:1300},
#     4:{1:0, 2:0},
# }
# age = 0
# kind = 0
# num = 0

# while True:
#     print('버스 요금 입력')
#     print()
    
#     while True:
#         age = int(input('''8세 미만 : (0)    8세 이상-14세 미만 : (1)    14세 이상-20세 미만 : (2)    20세 이상 : (3)    75세 이상 : (4)
#         >>>  '''))
        
#         if age >= 0 and age <= 4:
#             break
    
#         else:
#             print("잘못 선택하셨습니다. 다시 선택해주세요!!")
#             continue   
    
    
#     while True:
#         kind = int(input('''카드 : (1)      현금 : (2)
#         >>>  '''))
 
#         if kind > 0 and kind < 3:
#             break
        
#         else:
#             print("잘못 선택하셨습니다.다시 선택해주세요!!")
#             continue
                        
#     if kind == 1:
#         kind = '카드'
#     elif kind == 2:
#         kind = '현금'
#     break
    
# print()
# print(f'나이: {age}세')
# print(f'지불유형: {kind}') 
# print('버스요금: ', table[age][kind],'원') 



