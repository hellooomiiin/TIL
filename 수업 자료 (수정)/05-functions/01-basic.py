# # 함수 정의

# def make_sum(pram1, pram2):
#     """이것은 두 수를 받아
#     두 수의 합을 변환하는 함수입니다.
#     >>> make_sum(1,2)
#     3    
#     """
#     return pram1 + pram2

# # 함수 호출 및 반환 값 할당

# sum_result = make_sum(100, 30)
# print(sum_result)

# # print() 함수는 반환값이 없다.
# '''
# 반환과 출력은 다름, 반환은 값을 가지고 있을 뿐 보여주지 않음 출력은 터미널에 보여주는 것
# '''

# return_value = print(1) # 오른쪽 출력 1, 반환 값은 None
# print(return_value) #None


# def say_hello(greeting):
#     print(greeting)

# say_hello(35)

# def greet(name, age=30):
#     print(f'안녕하세요, {name}님! {age}살이시군요.')

# greet('any', age=35)

# def calculate_sum(*args):
#     print(args)
#     print(type(args))

# calculate_sum(1, 30, 50, 70, 180, 900)

# def print_info(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# print_info(name = 'Eve', age = 45)

# def func(pos1, pos2, default_arg='default', *args, **kwargs):
#     print(pos1) #1
#     print(pos2) #2
#     print(default_arg) #3
#     print(args) #(4, 5, 6)
#     print(kwargs) #key1='value1', key2='value2'
#     print(type(args)) #tuple
#     print(type(kwargs)) #dict

# func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')

# pos1 = 1, pos2 = 2, default_arg = 3, kwargs = key1='value1', key2='value2', args = (4, 5, 6)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

