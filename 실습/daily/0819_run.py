import sys
sys.stdin = open("input.txt")

# 백준 8958

# T = int(input())
#
# for tc in range(1, T + 1):
#     arr = list(map(list, input().split('X')))
#
#     s = []
#
#     for i in arr:
#         i_len = len(i)
#         for num in range(1, i_len + 1):
#             s.append(num)
#
#     print(sum(s))

# N = 4
# result = []
#
# def recur(cnt):
#     if cnt == N:  # 모든 숫자를 고려했다면
#         print(*result)
#         return
#
# recur(0)

# 백준 4344

# C = int(input())
#
# for tc in range(1, C + 1):
#     lst = list(map(int, input().split()))
#     N = lst[0]
#     arr = lst[1:N + 1]
#
#     def avg(score_list):
#         return int(sum(score_list) / N)
#
#     count = 0
#
#     for num in arr:
#         if num > avg(arr):
#             count += 1
#
#     print(f'{round(count / N * 100, 3)}%')


# 백준 2738

# N, M = map(int, input().split())
# arr_1 = [list(map(int, input().split())) for _ in range(N)]
# arr_2 = [list(map(int, input().split())) for _ in range(N)]
#
# for i in range(N):
#     for j in range(M):
#         arr_1[i][j] += arr_2[i][j]
#     print(' '.join(map(str, arr_1[i])))

# for i in range(N):
#     for j in range(N):
#         for x in range(N):
#             for y in range(N):
#                 arr_1[i][j] += arr_2[x][y]
#                 break
#             break
#
# print(arr_1)

# 0820

# 큐 연습하기

# from collections import deque
## 덱을 쓰는 이유는 list는 앞에서 append나 pop 하면 메모리 이슈
#
# N = int(input())
# arr = list(input() for _ in range(N))
#
# my_q = deque()
#
# for i in range(N):
#     # print(arr[i].split())
#     temp = arr[i].split()
#
#     if temp[0] == 'enqueue':
#         my_q.append(int(temp[1]))
#     elif temp[0] == 'front':
#         if my_q[0]:
#             print(my_q[0])
#         else:
#             print(-1)
#     elif temp[0] == 'rear':
#         if my_q[-1]:
#             print(my_q[-1])
#         else:
#             print(-1)
#     elif temp[0] == 'dequeue':
#         if my_q[0]:
#             print(my_q.popleft())
#         else:
#             print(-1)
#     elif temp[0] == 'isEmpty':
#         if my_q:
#             print(-1)
#         else:
#             print(1)
#     elif temp[0] == 'size':
#         print(len(my_q))

# from collections import deque
#
# T = 10
# for tc in range(1, 11):
#     N = int(input())
#     arr = deque(list(map(int, input().split())))
#
#     i = 1
#
#     while 0 not in arr:
#         for i in range(1, 6):
#             pop_value = arr.popleft()
#             if pop_value - i > 0:
#                 arr.append(pop_value - i)
#             else:
#                 arr.append(0)
#                 break
#             if i == 5:
#                 i = 1
#                 continue
#             i += 1
#
#     print(f'#{tc}', end=' ')
#     for i in list(arr):
#         print(i, end=' ')
#     print()

# 백준 2566

# arr = [list(map(int, input().split())) for _ in range(9)]
#
# max_num = 0
# x = 0
# y = 0
#
# for i in range(9):
#     for j in range(9):
#         if arr[i][j] >= max_num:
#             max_num = arr[i][j]
#             x = i + 1
#             y = j + 1
# print(max_num)
# print(x, y)

# 백준 3052

# arr = [int(input()) for _ in range(10)]
#
# remainders = []
#
# for num in arr:
#     remainders.append(num % 42)
#
# c = []
#
# for remainder in remainders:
#     if remainder not in c:
#         c.append(remainder)
#
# print(len(c))

# 백준 2577

# A, B, C = [int(input()) for _ in range(3)]
#
# num = str(A * B * C)
# N = len(num)
#
# dat = [0] * 10

# swea 노드의 거리

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    S, G = map(int, input().split())

    # 재귀
    # def dfs(now):
    #     route.append(now)
    #     for next_node in graph[now]:
    #         if visited[next_node] == 1:
    #             continue
    #         visited[next_node] = 1
    #         dfs(next_node)

    from collections import deque

    def bfs(start):
        dq = deque([start])

        while dq:
            now = dq.popleft()

            for next_node in graph[now]:
                if visited[next_node]:
                    continue

                visited[next_node] = visited[now] + 1
                dq.append(next_node)

                if next_node == G:
                    print(f'#{tc} {visited[G] - 1}')
                    break


    route = []

    # 방문
    visited = [0] * (V + 1)
    visited[1] = 1

    bfs(S)