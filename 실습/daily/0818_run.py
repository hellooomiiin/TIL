import sys
sys.stdin = open("input.txt")

# 탑 쌓기 게임

T = int(input())

for tc in range(1, T + 1):
    N, M1, M2 = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    M1_list = arr
    M2_list = []

    while len(M2_list) <= M2:
        M2_list.append(M1_list.pop(n))
        if n > 2:
            n += 1

    # for i in range(N):
    #     if len(M1_list) < M1:
    #         if i % 2 == 0:
    #             M1_list.append(arr[i])
    #     if len(M2_list) < M2:
    #         if i % 2 == 1:
    #             M2_list.append(arr[i])
    #
    # i = 0
    # for c in range(M2):
    #     M2_list.append(M1_list[i])
    #     i += 2
    #
    # M1_set = set(M1_list) - set(M2_list)
    # M1_list = list(M1_set)
    #
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