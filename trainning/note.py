import math

my_list = [[1,3,5,7], [1,2,3,4]]

print(list(map(sum, zip(*my_list))))
