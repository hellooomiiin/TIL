<<<<<<< HEAD
# # 딕셔너리 표현
# my_dict_1 = {}
# my_dict_2 = {'key':'value'}
# my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}
=======
# 딕셔너리 표현
my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}
>>>>>>> 0a53d7fb216732c9034bc7d4dee4c016c2a04824

# print(my_dict_1)  # {}
# print(my_dict_2)  # {'key': 'value'}
# print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}


# # 딕셔너리는 키에 접근해 값을 얻어냄
# my_dict = {'name': '홍길동', 'age': 25}
# print(my_dict['name'])  # '홍길동'
# print(my_dict['test'])  # KeyError: 'test'


# # 딕셔너리 값 추가 및 변경
# my_dict = {'apple': 12, 'list': [1, 2, 3]}
# # 추가
# my_dict['banana'] = 50
# print(my_dict)  # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}

# # 변경
# my_dict['apple'] = 100
# print(my_dict)  # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}

di = {}

di = {
    "name": "홍길동",
    (1, 2): "test"
}

print(di)

di[3] = 3


# arr = [1, 2, 3]
# 메모리에 연속되게 저장 -> 빠르게 인덱스로 접근이 가능하다.

# key 값은 불변 데이터만 가능 (list는 불가능하다!)
# key 값이 변동 -> 해시값이 변동 -> 

# 키 값이 있는지 검사
print(di.get(3))