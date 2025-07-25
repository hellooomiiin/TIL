<<<<<<< HEAD
# # 리스트 표현
# my_list_1 = []
# my_list_2 = [1, 'a', 3, 'b', 5]
# my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
=======
# 리스트 표현
my_list_1 = []
my_list_2 = [1, 'a', 3, 'b', 5]
my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
>>>>>>> 0a53d7fb216732c9034bc7d4dee4c016c2a04824

# my_list = [1, 'a', 3, 'b', 5]

# # 인덱싱
# print(my_list[1])  # a

# # 슬라이싱
# print(my_list[2:4])  # [3, 'b']
# print(my_list[:3])  # [1, 'a', 3]
# print(my_list[3:])  # ['b', 5]
# print(my_list[::2])  # [1, 3, 5]
# print(my_list[::-1])  # [5, 'b', 3, 'a', 1]

# # 길이
# print(len(my_list))  # 5

# # 중첩된 리스트 접근
# my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
# print(len(my_list))  # 5
# print(my_list[4][-1])  # !!!
# print(my_list[-1][1][0])  # w

# # 리스트는 가변
# # 1. 인덱싱으로 값 수정
# my_list = [1, 2, 3, 4, 5]
# my_list[1] = 'two'
# print(my_list)  # [1, 'two', 3, 4, 5]

# # 2. 슬라이싱으로 값 수정
# my_list = [1, 2, 3, 4, 5]
# my_list[2:4] = ['three', 'four']
# print(my_list)  # [1, 2, 'three', 'four', 5]


numbers = []

numbers.append(3) # append: 가장 뒤에 데이터를 추가
numbers.append(2)
numbers.append(1)
numbers.append(5)

numbers.pop() # pop(): 맨 뒤의 데이터 삭제
print(numbers)

# print(numbers[0])
# print(numbers[-1])
# print(numbers[0:2])
# print(numbers[::2])
