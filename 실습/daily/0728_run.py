import first

# def func():

# as (alias) : 별명을 지어주는 개념

result = [num * 2 for num in range[1, 11] if num % 2 == 0]

print(result)

# 두 리스트의 모든 조합 만들 때
colors = ["red", "blue"]
size = ["S", "M", "L"]

result2 = [for color in colors for size in size]

result3 = [list(map(int, input().split())) for i in range(3)]

# 입력값에 활용

N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
for i in range(9):
    arr_1.append(data_1[i])

print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
arr_2 = data_2.split()
for i in arr_2:
        if int(i) % 2 != 0:
                print(i)


list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]


for book in rental_list:
        if book not in list_of_book:
            print(f'{book} 은/는 보유하고 있지 않습니다.')
            break
else:
    print("모든 도서가 대여 가능한 상태입니다.")


# 아래 함수를 수정하시오.

def reverse_string(string):
    chars = list(string) # ['H', 'e', ... ]
    chars.reverse() # ['!', 'd', ... ]
    return ''.join(chars)
result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH

data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
for i in data_1:
    if i.isupper() == True or i == ' ':
        print(i, end='')


data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
sen = ['내', '힘', '들', '다']
for i in sen:
        index = (data_2.find(i))
        arr.append(index)
print()
print(arr)

arr.sort()
print(arr) # [5, 12, 29, 37]

for i in arr:
    print(data_2[i], end='')



# 아래 함수를 수정하시오.
# - __init__(생성자, 매직 메서드)
def remove_duplicates(lst):
    new_lst = set(lst)
    new_lst = list(new_lst)
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)

li = [1, 10000, 20000, 30000, 20000, 20000]

# di = {}
# di = {1:1}
# di = {1:1, 10000: 1}
# di = {1:1, 10000: 1, 20000: 3, 30000: 1}
di = {}

for i in li:
    # i 라는 숫자가 기존 딕셔너리에 있었다면, value + 1
    # i 라는 숫자가 기존 딕셔너리에 없었다면, key : 1
    if di.get(i): # di가 i를 가지고 있다면
        di[i] += 1
    else:
        di[i] = 1

print(di)
print(list(di))

# 아래 함수를 수정하시오.
def remove_duplicates(lst):
    new_lst = set(lst)
    new_lst = list(new_lst)
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)




def remove_duplicates(lst):
    my_dict = {}
    for i in lst:
        if my_dict.get(i):
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
print(list(result))