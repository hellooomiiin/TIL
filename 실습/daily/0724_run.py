# def step1(cm):
#     if cm >= 140:
#         print("탑승 가능합니다.")
#     else:
#         print("탑승 불가입니다.")

# step1(150)

# def step2(age, cm):
#     # 두 조건을 모두 만족해야만 탑승 가능 -> and
#     if age >= 12 and cm >= 140:
#         print("탑승 가능합니다.")
#     else:
#         print("탑승 불가입니다.")

# def step2_1(age, cm):
#     # 두 조건을 모두 만족해야만 탑승 가능 -> and
#     if age >= 12:
#         if cm >= 140:
#             print("탑승 가능합니다.")
#         else:
#             print("키가 작아 탑승 불가입니다.")
#     else:
#         print("나이가 어려 탑승 불가입니다.")

# step2(10, 160)
# step2_1(12, 139)

# def step3(age, cm, y_or_n):
#     if cm >= 140:
#         if age >= 12:
#             print("탑승 가능합니다.")
#         else:
#             if y_or_n == True:
#                 print("보호자 동반해 탑승 가능합니다.")
#             else: 
#                 print("보호자 미동반으로 탑승 불가합니다.")
#     else:
#         print("키 제한으로 탑승 불가입니다.")

# y = True
# n = False

# step3(10, 150, y)

# numbers = [2, 3, 4, 5, 6]

# for number in numbers:
#     print(number)

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)
# continue는 뒷 코드 패스 느낌
    
def solution(n):
    total = 0 #누적합
    now = 1 #1부터 증가할 변수

    while total < n:
        total += now
        now += 1

    print(f'누적 합이 {n} 이상이 된 시점 마지막 숫자 = {now - 1}')

solution(10)





# outers = ['A', 'B']
# inners = ['c', 'd']

# for outer in outers:
#     for inner in inners:
#         print(outer, inner)






# # 아래에 코드를 작성하시오.
# from 