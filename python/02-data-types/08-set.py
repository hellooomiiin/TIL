# <<<<<<< HEAD
# # # 세트 표현
# # # my_set_1 = 
# # # my_set_2 = 
# # # my_set_3 = 
# =======
# # 세트 표현
# my_set_1 = set()
# my_set_2 = {1, 2, 3}
# my_set_3 = {1, 1, 1}
# >>>>>>> 0a53d7fb216732c9034bc7d4dee4c016c2a04824

# # print(my_set_1)  # set()
# # print(my_set_2)  # {1, 2, 3}
# print(my_set_3)  # {1}


# # 세트의 집합 연산산
# my_set_1 = {1, 2, 3}
# my_set_2 = {3, 6, 9}

# # 합집합
# print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}

# # 차집합
# print(my_set_1 - my_set_2)  # {1, 2}

# # 교집합
# print(my_set_1 & my_set_2)  # {3}

a = {1, 2, 3}
b = {2, 3, 4}

print(a | b) #합집합
print(a & b) #교집합
print(a - b) #차집합
print(a ^ b) #대칭차집합

c = set()
d = {}
print(type(c))
print(type(d))

e = {1, 2}
f = {2, 1}
print(e == f)

g = {1, 5}
h = {1, 2, 3, 4}

print(g < h)