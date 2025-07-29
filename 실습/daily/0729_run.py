my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.
for i in my_set:
    if i in my_dict:
        print(my_dict.get(i))
    else:
        print("None")

var = (1, 2, 3, 'A')
my_dict[var] = '변수로도 키 설정 가능'
print(my_dict)

data = {
    '이름': '키위',
    '종류': '새',
    '원산지': '호주' 
}

plus_data = {
    '종류': '과일',
    '가격': 30000
}
# 1. data가 가진 모든 키와 벨류 목록을 출력한다.

# 2. data가 가진 벨류 목록들만 모아서 출력한다.

# 3. data에서 'without' 키가 가진 value를 출력한다.
    # 해당하는 키가 data에 없다면, 'unknown' 문자열을 출력한다.

# 4. plus_data가 가진 모든 키와 벨류를 data에 추가한다.

# 5. 변경된 data를 출력한다.

print(data.items())
print(data.values())
print(data.get('without', 'unknown'))
data.update(plus_data)
print(data)

data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
for i in data:
    for key in key_list:
        i.setdefault(key, 'unknown')
        print(f'{key}은/는 {i.get(key)}입니다.')

# 아래 함수를 수정하시오.
def remove_duplicates_to_set(lst):
    return set(lst)


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)

# 아래 함수를 수정하시오.
def union_sets(set_1, set_2):
    return set_1.union(set_2)

def union_multiple_sets(*sets):
    if len(sets) < 2:
        print("최소 두 개의 셋이 필요합니다.")
    else:
        union_1 = sets[0] #{1, 2}
        for set in sets[1:]:
            union_1 = union_1.union(set)
        return union_1



result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
# # 출력 : 최소 두 개의 셋이 필요합니다

