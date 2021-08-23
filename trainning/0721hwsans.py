#homework
#1번
#빌트인 함수


#2번
# sen = input('단어를 입력하세요: ')

# def str_mid(a):
#     if len(a) % 2:
#         return a[len(a) // 2]
#     else:
#         return a[(len(a) // 2 -1):len(a) // 2 +1]

# print(str_mid(sen))



# def get_middle_char(string):
#     length = 0
#     for char in string:
#         length += 1
    
#     idx = length // 2
#     if length % 2:

#         return string[idx]
#     else:
#         return string[idx-1:idx+1]

# print(get_middle_char('ssafy'))
# print(get_middle_char('coding'))

#3번
#(4)번

#4번
#None

#5번

def my_avg(*numbers):
    total = 0
    length = 0
    for num in numbers:
        total += num
        length += 1

    return total / length

avg = my_avg(77, 83, 95, 80, 70)
print(avg)


#workshop
#1번

def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num

    return total

print(list_sum([1,2,3,4,5]))


#2번
# dict_a = [
#     {'name': 'kim', 'age': 12},
#     {'name': 'lee', 'age': 4}
# ]
# def dict_list_sum(dict_list):
#     total = 0
#     for dictionary in dict_list:
#         total += dictionary['age']

#     return total

# print(dict_list_sum(dict_a))

#가변 키워드 인자 예시
# def test_def(**kwargs):
#     print(kwargs)

# test_def(a=10, b='asdf', c='!!!!', d=[1,2,3])


#3번
def all_list_sum(num_list):
    total = 0
    for numbers in num_list:
        for number in numbers:
            total += number
    
    return total

result = all_list_sum([[1], [2,3], [4,5,6], [7,8,9,10]])
print(result)