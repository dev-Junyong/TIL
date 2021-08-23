#1.1
# students = ['김철수', '이영희', '조민지']

# print(len(students))

# result = 0

# for student in students:
#     result += 1

# print(result)

#1.2
# students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
# cnt = 0
# for student in students:
#     if student == '이영희':
#         cnt += 1

# print(cnt)


#1.3
# numbers = [7, 10, 22, 4, 3, 17]

# print(max(numbers))
# max_num = 0
# for number in numbers:
#     if number >= max_num:
#         max_num = number

# print(max_num)

# numbers = [-1,-3,-100]

# max_num = numbers[0]
# for number in numbers:
#     if number > max_num:
#         max_num = number

# print(max_num)

#1.4
# numbers = [7, 10, 22, 4, 3, 17]
# print(min(numbers))

# min_num = numbers[0]
# for number in numbers:
#     if number <= min_num:
#         min_num = number

# print(min_num)

#1.5
# numbers = [7, 10, 22, 7, 22, 22]

# max_num = numbers[0]
# cnt = 0
# for number in numbers:
#     if number > max_num:
#         max_num = number
#         cnt = 1
#     elif number == max_num:
#         cnt += 1

# print(f'{max_num}, {cnt}')
# print(max_num, cnt)

#1.6
# numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

# # a = numbers.count(5)
# # print(a)

# cnt = 0
# for number in numbers:
#     if number == 5:
#         cnt += 1

# print(cnt)


#1.7
# word = input()
# word_li = ''
# for char in word:
#     if char == 'a':
#         continue
#     else:
#         word_li += char

# print(word_li)

# word = input()

# result = ''
# for char in word:
#     if char != 'a':
#         result += char

# print(result)


#1.8
# word = input()

# result = ''
# for char in word:
#     result = char + result

# print(result)

# print(word[::-1])


#hws 0719 - 0721
# import keyword
# print(keyword.kwlist)

# import math

# num1 = 0.1*3
# num2 = 0.3

# result = abs(num1 - num2) < 1e-10
# print(result)

# print(math.isclose(num1,num2))


# name = '철수'
# print(f'안녕, {name}야')


# n = int(input('가로 길이 입력: '))
# m = int(input('세로 길이 입력: '))

# print(("*" * n + "\n") * m)


# print('"파일은 c:\\window\\User\\내문서\\Python에 저장이 되었습니다."',"\n","나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'"  )


# num = int(input("자연수 입력: "))

# for i in range(1, num+1):
#     print(i)


# num = int(input("자연수 입력: "))

# while num >= 0:
#   print(num)
#   num -= 1


# num = int(input("숫자를 입력: "))
# total = 0
# for n in range(0, num+1):
#     total += n

# print(total)


# for i in range(1, 51):
#     if i % 2:
#         print(i)



# n = int(input('가로 길이: '))
# m = int(input('세로 길이: '))

# for i in range(m):
#     for j in range(n):
#         print('*', end='')
#     print()



# temp = 36.5

# print('입실 불가') if temp >= 37.5 else print('입실 가능')


# scores = [80, 89, 99, 83]
# total = 0 
# cnt = 0
# avg_score = 0

# # for score in scores:
# #     total += score
# #     cnt += 1

# # print(total / cnt)

# for score in scores:
#     total += score

# cnt = int(len(scores))
# print(total / cnt)



# num = int(input('숫자를 입력(1이상 1000이하): '))

# for i in range(1, num+1):
#     if num % i == 0:
#         print(i, end=' ')



# numbers = [
#     85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
#     51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
#     52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
# ]

# length = 0
# for num in numbers:
#     length += 1

# center = length // 2
# sort_list = sorted(numbers)
# print(sort_list[center])

# while len(numbers) > 1:
#     numbers.remove(max(numbers))
#     numbers.remove(min(numbers))

# print(numbers[0])



# for i in range(len(numbers) -1, 0, -1):
#     for j in range(i):
#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# mid_number = int(numbers[len(numbers) // 2])
# print(mid_number)



# num = int(input('자연수 입력: '))
# for i in range(num):
#     for j in range(1, i+2):
#         print(f'{j}', end='')
#     print()


# num = int(input('숫자 입력: '))

# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(f'{j}', end = '')
#     print('')




# sen = input('단어를 입력하세요: ')

# def get_middle_char(string):
#     if len(string) % 2:
#         return string[len(string) // 2]
#     else:
#         return string[(len(string)//2 -1):len(string)//2 +1]

# print(get_middle_char(sen))


# sen = input('단어를 입력하세요: ')
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



# def my_avg(*args):
#     total = 0
#     avg = 0
#     len1 = len(args)
#     for i in args:
#         total += i

#     return total / len1

# avg_list = [77, 83, 95, 80, 70]
# print(my_avg(*avg_list))


# def my_avg(*numbers):
#     total = 0
#     length = 0
#     for num in numbers:
#         total += num
#         length += 1

#     return total / length

# avg = my_avg(77, 83, 95, 80, 70)
# print(avg)


# def list_sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# print(list_sum([1,2,3,4,5]))



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



# list_b = [[1], [2,3], [4,5,6], [7,8,9,10]]

# def all_list_sum(num_list):
#     total = 0
#     for numbers in num_list:
#         for number in numbers:
#             total += number
#     return total

# print(all_list_sum(list_b))



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




#practice1,2,3
# def my_abs(x):
#     # 1. 복소수이면, 
#     if type(x) == complex:
#     # if type(x) is complex:
#     # if isinstance(x, complex): 비교하는 또다른 방법, OOP 수업에서 다룰 것이다.
#         return (x.imag**2 + x.real**2) ** (1/2)
#     # 2. 복소수가 아니면,
#     else:
#         if x == 0:
#             return x ** 2
#         if x < 0:
#             return x * -1
#         else:
#             return x

# print(my_abs(3+4j))
# print(my_abs(-0.0))
# print(my_abs(-5))
# print(abs(3+4j), abs(-0.0), abs(-5))



# def my_all(elements):
#     result = True
#     for element in elements:
#         if not element:
#             result = False
#             break
#     return result


# def my_all(elements):
#     for element in elements:
#         if not element:
#             return False
#     return True

# print(my_all([]))
# print(my_all([1, 2, 5, '6']))
# print(my_all([[], 2, 5, '6']))
# print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))



# def my_any(elements):
#     for element in elements:
#         if element:
#             return True
#     return False

# print(my_any([1, 2, 5, '6']))
# print(my_any([[], 2, 5, '6']))
# print(my_any([0]))
# print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any([0]))




# def snail(height, day, night):
#     count = 0
#     while True:
#         count += 1
#         height -= day
#         if height <= 0:
#             return count
#         height += night

# print(snail(100,5,2))


# def sum_of_digit(number):
#     total_sum = 0
#     while number / 10:
#         # 아래의 코드는 number, remainder = divmod(number, 10) 으로 변경 가능하다.
#         remainder = number % 10
#         number = number // 10
#         total_sum += remainder
#     return total_sum

# print(sum_of_digit(1234))
# print(sum_of_digit(1230))
# print(sum_of_digit(4321))


# def sum_of_digit(number):
#     if number < 10:
#         return number
#     else:
#         number, remainder = divmod(number, 10)
#         return sum_of_digit(number) + remainder

# print(sum_of_digit(1234))
# print(sum_of_digit(1230))
# print(sum_of_digit(4321))



# def is_pal_while(word):
#     while len(word) > 1:
#         if word[0] == word[-1]:
#             word = word[1:-1]
#         else:
#             return False
#     return True

# print(is_pal_while('tomato'))
# print(is_pal_while('racecar'))
# print(is_pal_while('azza'))

# def is_pal_recursive(word):
#     if len(word) <= 1:
#         return True
#     if word[0] == word[-1]:
#         return is_pal_recursive(word[1:-1])
#     else:
#         return False

# print(is_pal_recursive('tomato'))
# print(is_pal_recursive('racecar'))
# print(is_pal_recursive('azza'))




# def get_secret_word(numbers):
#     result = ''
#     for num in numbers:
#         result += chr(num)
        
#     return result

# list_a = [83, 115, 65, 102, 89]
# print(get_secret_word(list_a))



# def get_secret_number(word):
#     result = 0
#     for char in word:
#         result += ord(char)
#     return result


# list_str = 'tom'
# print(get_secret_number(list_str))



# def get_strong_word(word1, word2):
#     sum1 = get_secret_number(word1)
#     sum2 = get_secret_number(word2)

#     if sum1 >= sum2:
#         return word1
#     else:
#         return word2
# res1 = get_strong_word('z', 'a')
# res2 = get_strong_word('tom', 'john')

# print(res1)
# print(res2)


user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}

print(user_data1['password'])

