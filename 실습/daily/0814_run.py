import sys
sys.stdin = open("input.txt")

# 계산기1

# 1. 중위 -> 후위표기법으로 바꾸는 함수
# def infix_to_postfix(tokens):
#     stack = [] # 후위표기법 최종 결과
#     oper_stack = [] # 연산자들이 중간에 거쳐갈 스택

    # for token in tokens:
        # 1. 숫자라면, 그냥 stack에 쌓는다
        # 2. 연산자라면
        # - oper stack 에 연산자가 있는지 확인
        # - 있다면, 기존 연산자를 꺼내서 stack에 집어넣는다.
        #   - 기존 연산자를 꺼내서 stack에 넣는다.
        #   - 현재 연산자를 oper_stack에 넣는다.
        # - 없다면, oper_stack에 추가


    # return stack


# for tc in range(1, 2):
#     N = int(input())
#     row = input()
#
# # 2. 후위표기법을 계산하는 함수
# def calculate(tokens):
#     stack = []
#
#     for token in tokens:
#         # 숫자라면, stack에 넣는다
#         if token.isdigit():
#             stack.append(int(token))


# 콜라츠 추측

# T = int(input())
#
# for tc in range(1, T + 1):
#
#     N = int(input())
#
#     count = 0
#
#     def recur(n):
#         global count
#         if n == 1:
#             return count
#         if n % 2 == 0:
#             count += 1
#             n //= 2
#             return recur(n)
#         if n % 2 != 0:
#             count += 1
#             n = n * 3 + 1
#             return recur(n)
#
#     print(f'#{tc} {recur(N)}')

# 탑 쌓기 게임

T = int(input())

for tc in range(1, T + 1):
    N, M1, M2 = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    M1_list = arr
    M2_list = []

    i = 0
    for c in range(M2):
        M2_list.append(M1_list[i])
        i += 2

    M1_set = set(M1_list) - set(M2_list)
    M1_list = list(M1_set)

    s = 0

    for num in M1_list:
            s += num * (M1_list.index(num) + 1)
    for num in M2_list:
            s += num * (M2_list.index(num) + 1)

    print(f'#{tc} {s}')

    # M1_list에서 M2만큼 꺼내오면 됨
    # 원래 맨 밑에 있는 애는 두고 그 다음꺼

    # 그냥 sort 때려서 큰 수부터 각각 한 번씩 나눠줌 조건 : 공간이 남았을 때! 비교문문



    # while len(M1_list) != M1:
    #     if arr.index(i) % 2 == 0:
    #         M1_list.append(i)
    # while len(M2_list) != M2:
    #         if arr.index(i) % 2 ==1:
    #             M2_list.append(i)
    # s = 0
    #
    # for num in M1_list:
    #         s += num * (M1_list.index(num) + 1)
    # for num in M2_list:
    #         s += num * (M2_list.index(num) + 1)
    #
    # print(f'#{tc} {s}')
