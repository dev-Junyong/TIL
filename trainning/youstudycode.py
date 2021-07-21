# #workshop
# #1번

# list_a = [1,2,3,4,5]

# def list_sum(a):
#     sum = 0
#     for i in a:
#         sum = sum + i
#     return sum

# print(list_sum(list_a))


# #2번
# dict_a = [
#     {'name': 'kim', 'age': 12},
#     {'name': 'lee', 'age': 4}
# ]

# def dict_list_sum(a):
#     total = 0
#     for i in a:
#         total += i['age']
#     return total

# print(dict_list_sum(dict_a))


# #3번
# list_b = [[1], [2,3], [4,5,6], [7,8,9,10]]

# def all_list_sum(a):
#     total = 0
#     for i in a:
#         if type(i) == list:
#             total += all_list_sum(i)
#         else:
#             total += i
#     return total

# print(all_list_sum(list_b))


#homework
#1번

#2번
# sen = input('단어를 입력하세요: ')

# def str_mid(a):
#     if len(a) % 2:
#         return a[len(a) // 2]
#     else:
#         return a[(len(a) // 2 -1):len(a) // 2 +1]

# print(str_mid(sen))

#3번

# def study1(name, location='서울'):
#     print(f'{name}의 지역은 {location}입니다.')

# print(study1('허준'))

# print(study1(location='대전', name='철수'))

# print(study1('영희', location='광주'))

# # print(study1(name='길동', '구미'))


#4번
# def my_func(a,b):
#     c = a + b
#     print(c)

# result = my_func(3,7)
# print(result)


#5번

def my_avg(*args):
    total = 0
    avg = 0
    len1 = len(args)
    for i in args:
        total += i

    return total // len1

avg_list = [77, 83, 95, 80, 70]
print(my_avg(*avg_list))

