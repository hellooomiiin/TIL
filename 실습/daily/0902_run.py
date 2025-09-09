import sys
sys.stdin = open("input.txt")

# 백준 2577

# A, B, C = [int(input()) for _ in range(3)]
#
# value = str(A * B * C)
#
# dat = [0] * 10
#
# for ch in value:
#     i = int(ch)
#     dat[i] += 1
#
# for c in dat:
#     print(c)

# 백준 10798

# arr = [list(input()) for _ in range(5)]
#
# for i in range(5):
#     if len(arr[i]) < 15:
#         for _ in range(15 - len(arr[i])):
#             arr[i].append('')
#
# for j in range(15):
#     for i in range(5):
#         if arr[i][j] != '':
#             print(arr[i][j], end='')
#         else:
#             continue
#
# print(arr)

# arr[0][0] [1][0] [2][0]
# [0][1] [1][1] [2][1]

# 경비원

# N, M = map(int, input().split())
# total = int(input())
# arr = [list(map(int, input().split())) for _ in range(total)]
# start = list(map(int, input().split()))
#
# s = 0
#
# for i in range(total):
#     if start[0] == 1 or 2:
#         if arr[i][0] == start[0]:
#             s += abs(arr[i][1] - start[1])
#         elif arr[i][0] == 1:
#             s += start[1] + M + arr[i][1]
#         elif arr[i][0] == 3 or 4:
#                 s += start[1] + arr[i][1]
#     elif start[0] == 3 or 4:
#         if arr[i][0] == start[0]:
#             s += abs(arr[i][1] - start[1])
#         elif arr[i][0] == 3 or 4:
#             if start[0] > N // 2:
#                 s += start[1]
#                 s += arr[i][1]
#
# print(s)

# N과 M 문제

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
#
# arr.sort()
#
# path = []
# visited = [False] * N
#
#
# def recur(cnt, p):
#     if cnt == M:
#         print(*path)
#         return
#     prev = 0
#     for i in range(p, N):
#         # if visited[i]:
#         #     continue
#         if arr[i] == prev:
#             continue
#         prev = arr[i]
#         visited[i] = True
#         path.append(arr[i])
#         recur(cnt + 1, i)
#         path.pop()
#         visited[i] = False
#
#
# recur(0, 0)

# 팩토리얼

# N = int(input())
#
#
# def recur(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 1
#     return n * recur(n - 1)
#
#
# print(recur(N))

# N 캐슬

# T = 10
#
# for tc in range(1, 11):
#     N = int(input())
#
#     def recur(n):
#         if n == 1:
#             return 1
#         return n * recur(n - 1)
#
#     print(f'#{tc} {recur(N)}')

# N 퀸


# def check(row, col):
#     # 상 좌상 우상
#     di = [-1, -1, -1]
#     dj = [0, -1, 1]
#
#     # 방향을 다 돌면서
#     for i in range(3):
#         ni, nj = row + di[i], col + dj[i]  # ~ 방향으로 한 칸 움직임
#         while 0 <= ni < N and 0 <= nj < N:
#             if visited[ni][nj] == 1:
#                 return False
#             ni += di[i]
#             nj += dj[i]
#
#     return True
#
#     # 같은 col 에 놓은 적이 있는가 ? 있으면 return False
#     # 좌상단 대각선에 놓은 적이 있는가 ? 있으면 return False
#     # 우상단 대각선에 놓은 적이 있는가 ? 있으면 return False
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     visited = [[0] * N for _ in range(N)]
#     result = 0
#
#     def path(row):
#         global result
#         if row == N:  # N 행을 모두 고려함
#             result += 1  # 경우의 수 + 1
#             return
#
#         # 이미 row 선택했고
#         for col in range(N):
#             if check(row, col):
#                 visited[row][col] = 1
#                 path(row + 1)
#                 visited[row][col] = 0  # 리셋
#
#     path(0)
#     print(f'#{tc} {result}')

# 증가하는 사탕 수열

# T = int(input())
#
# for tc in range(1, T + 1):
#     A, B, C = map(int, input().split())
#
#     cnt = 0
#
#     if C < 3:
#         cnt = -1
#         print(f'#{tc} {cnt}')
#         continue
#
#     if B >= C:
#         cnt += (B - C + 1)
#         B = C - 1
#
#     if A >= B:
#         cnt += (A - B + 1)
#         A = B - 1
#
#     if A < 1 or B < 1:
#         cnt = -1
#
#     print(f'#{tc} {cnt}')

# 전봇대

# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [tuple(map(int, input().split())) for _ in range(N)]

    # lines = []
    # ds = []
    #
    # for row in range(N):
    #     if arr[row][0] == arr[row][1]:
    #         lines.append(arr[row][0])
    #     else:
    #         ds.append(arr[row])
    #
    # cnt = 0
    #
    # for d in ds:
    #     for i in range(d[0], d[1] + 1):
    #         if i in lines:
    #             cnt += 1
    #
    #     for
    #
    # print(f'#{tc} {cnt}')

    # arr.sort(key=lambda x: (x[0]))
    #
    # cnt = 0
    #
    # for i in range(N):
    #     for j in range(i + 1, N):
    #         if arr[i][1] > arr[j][1]:
    #             cnt += 1
    #
    # print(f'#{tc} {cnt}')
