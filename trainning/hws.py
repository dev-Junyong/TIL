# #2번
# numbers = list(range(1,51))

# odd = numbers[::2]
# print(odd)

# #3번
# #숫자는 '' 제거
# students = {
#     '준용': 28
# }

# #4번
# n = int(input('가로길이'))
# m = int(input('세로길이'))

# for i in range(m):
#   for j in range(n): 
#         print('*', end='')
#   print('')

# #5번
# temp = 36.5
# print('입실 불가') if temp >= 37.5 else print('입실 가능')

# #6번
# scores = [80, 89, 99, 83]
# #개수, 총합
# total = 0
# count = 0
# for score in scores:
#     total += score
#     count += 1

# avg = total / count
# print(avg)

# #workshop
# #1번
# user_input = int(input('숫자 입력(1이상 1,000이하): '))

# for i in range(1, user_input+1):
#     if user_input % i == 0:
#         print(i, end=' ')

#2번
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

#또다른 풀이
# while len(numbers) > 1:
#     numbers.remove(max(numbers))
#     numbers.remove(min(numbers))

# print(numbers[0])


#3번

user_input = int(input('숫자'))

for i in range(user_input):
  for j in range(1, i+2): 
        print(f'{j}', end='')
  print('')

