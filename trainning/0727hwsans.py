#homework 
#1번
sorted([])
# 원본을 변경하지 않음, 정렬된 값을 반환
[].sort()
# 원본을 변경함

# reversed() / reverse()

#2번
a = []
a.append('abc') # ['abc']
# 인자의 값을 그대로 리스트 마지막에 추가
a.extend('abc') # ['a','b','c']
# 인자의 요소를 리스트에 더해줌



#3번
a = [1,2,3,4,5]
b = a
a[2] = 5
print(a)
print(b)

# 리스트의 요소는 같다, 같은 주소를 참조하기 때문

# shallow copy를 하는 법 / 슬라이싱, 리스트(), copy.copy
# 딥카피는 / copy.deepcopy





#workshop
#1번
def duplicated_letters(word):
    result = []
    for char in word:
        if word.count(char) > 1 and char not in result:
            result.append(char)

    return result # 조건문으로 중복되는 값이 들어가지 않도록 하는 방법
    # print(list(set(result))) set으로 리스트 중복 제거하는 방법
    # print(result)

a = 'apple'
b = 'banana'
print(duplicated_letters(a))
print(duplicated_letters(b))





#2번
def low_and_up(word):
    # length = len(word)
    # result = ''
    # for idx in range(length):
    #     if idx % 2: #홀수인 경우
    #         result += word[idx].upper()
    #     else:
    #         result += word[idx].lower()
    # return result

    #리스트 컴프리핸션 + 조건 표현식
    result = [char.upper() if idx%2 else char.lower() for idx, char in enumerate(word)]
    return ''.join(result)

a = 'apple'
b = 'banana'
print(low_and_up(a))
print(low_and_up(b))





#3번
def lonely(numbers):
    # result = [numbers[0]]
    # for num in numbers:
    #     if result[-1] != num:
    #         result.append(num)

    # return result

    # enumerate 사용방법
    result = []
    for idx, num in enumerate(numbers):
        if idx == 0:
            result.append(num)

        elif result[-1] != num:
            result.append(num)

    return result

list_a = [1,1,3,3,0,1,1]
list_b = [4,4,4,3,3]
print(lonely(list_a))
print(lonely(list_b))




