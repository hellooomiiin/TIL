import sys
sys.stdin = open("input.txt")

# 달팽이 문제
# 델타 + 조건 2개 1. 벽을 만나면 방향을 바꿀 것 2. 이미 숫자가 차있으면 방향을 바꿀 것

T = 10

for tc in range(1, 11):


    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    arr = [[0] * N for _ in range(N)]

    i, j = 0, 0
    dir_i = 0
    num = 1

    for _ in range(N * N):
        arr[i][j] = num
        num += 1

        ni = i + di[dir_i]
        nj = j + dj[dir_i]

        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj

        else:
            dir_i = (dir_i + 1) % 4
            i += di[dir_i]
            j += dj[dir_i]

    print(f'#{tc}')
    for i in arr:
        print(' '.join(map(str, i)))

# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_result = 0
#     ry, rx = 0, 0
#
#     # 전체 이차원 리스트를 순회하면서
#     for y in range(N):
#         for x in range(N):
#             # 상하좌우 값들을 더해준다.
#             result = arr[y][x]  # 현재좌표
#
#             for i in range(4):
#                 ny = y + dy[i]
#                 nx = x + dx[i]
#
#                 # 범위 밖으로 나가면, 해당 방향은 계산 X
#                 if ny < 0 or ny >= N or nx < 0 or nx >= N:
#                     continue
#
#                 result += arr[ny][nx]
#
#             # 최대값 갱신
#             if max_result < result:
#                 max_result = result
#                 ry = y
#                 rx = x
#
#     print(f'#{tc} {max_result} {ry} {rx}')

    #     arr = [[0] * N for _ in range(N)]
    #
    #     # for i in arr:
    #     #     print(i)
    #
    #     for num in range(1, N * N + 1):
    #         if num <= (N - 1) * 4:
    #             while num < N:
    #
    #                 arr.append()
    #                 num += 1
    # print(arr)
    # while N <= num:


T = 10

for tc in range(1, 11):
    tc_num = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 도착점(2) 찾기
    for i in range(100):
        if arr[99][i] == 2:
            goal_idx = i
            # print(goal_idx)

    # 방향 설정 (우좌상)
    di = [0, 0, -1]
    dj = [1, -1, 0]

    # 가능한 출발 지점 리스트 (필요 X)
    pos_start = []
    for i in range(100):
        if arr[0][i] == 1:
            pos_start.append(i)
            print(pos_start)

    # 밑에서부터 올라오도록 구현
    # while문, 종료 조건 : y 좌표가 0일 때까지 조건 만족할 때까지 돌아야 함

    # ?
    sart_idx = (99, goal_idx)
    dir_i = 0

    for _ in range(N * N):
        arr[i][j] = num
        num += 1


    ni = i + di[dir_i]
    nj = j + dj[dir_i]

    num = 1

    for _ in range(N * N):
        arr[i][j] = num
        num += 1

        ni = i + di[dir_i]
        nj = j + dj[dir_i]

        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj

        else:
            dir_i = (dir_i + 1) % 4
            i += di[dir_i]
            j += dj[dir_i]

    print(f'#{tc}')
    for i in arr:
        print(' '.join(map(str, i)))


# 일단 먼저 코드 말고 한국어로 구현하기
