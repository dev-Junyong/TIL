
# def count_vowels(word):

#     word1 = word.count('a')
#     word2 = word.count('i')    
#     word3 = word.count('e')
#     word4 = word.count('o')
#     word5 = word.count('u')
#     cnt = word1 + word2 + word3 + word4 + word5
#     return cnt

# print(count_vowels('apple'))
# print(count_vowels('banana'))


def only_square_area(a, b):


    num_list = []
    num_list1 = []
    for i in a:
        if i in b:
             num_list.append(i)

    for j in num_list:
        area = j*j
        num_list1.append(area)

    return num_list1


list1 = [32,55,63]
list2 = [13,32,40,55]

print(only_square_area(list1, list2))



# def get_dict_avg(a):
#     num_list = list(a.values())
#     total = 0
#     for i in num_list:
#         total += i
#     avg_num = total / len(num_list)

#     return avg_num


# dict_a = {
#     'python': 80,
#     'algorithm': 90,
#     'django': 89,
#     'web': 83,
# }
# print(get_dict_avg(dict_a))



# def count_blood(bloods):
#     cnt_a = 0
#     cnt_b = 0
#     cnt_o = 0
#     cnt_ab = 0
#     dict_a = {}
#     for blood in bloods:
#         if 'A' in blood:
#             cnt_a += 1
#         elif 'B' in blood:
#             cnt_b += 1
#         elif 'O' in blood:
#             cnt_o += 1
#         else:
#             cnt_ab += 1

#     dict_a['A'] = cnt_a
#     dict_a['B'] = cnt_b
#     dict_a['O'] = cnt_o
#     dict_a['AB'] = cnt_ab

#     return dict_a

# list_a = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']
# print(count_blood(list_a))

