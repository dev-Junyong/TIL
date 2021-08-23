# a = [1,2,3,4,5]
# b = a

# a[2] = 5

# print(a)
# print(b)


# def low_and_up(word):
#     answer = ''
#     idx = 0
#     for i in word:
#         if i == ' ':
#             answer += ' '
#             idx = 0
#         else:
#             if idx == 1:
#                 answer += i.upper()
#                 idx = 0
#             elif idx == 0:
#                 answer += i.lower()
#                 idx = 1
    
#     return answer

# a = 'apple'
# b = 'banana'
# print(low_and_up(a))
# print(low_and_up(b))



# def duplicated_letters(word):
#     chk = ''
#     for i in range(len(word)-1):
#         for j in range(i+1, len(word)):
#             if word[i] == word[j]:
#                 chk += word[i]
#                 return chk
    
# a = 'apple'
# b = 'banana'
# print(duplicated_letters(a))
# print(duplicated_letters(b))


def lonely(word):
    ans = []
    for i in range(len(word)):
        if i == 0:
            ans.append(word[i])
        elif word[i] != word[i-1]:
            ans.append(word[i])
    return ans

list_a = [1,1,3,3,0,1,1]
list_b = [4,4,4,3,3]
print(lonely(list_a))
print(lonely(list_b))
