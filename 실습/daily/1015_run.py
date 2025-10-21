import sys
sys.stdin = open("input.txt")

# LCS

# str_1 = list(input())
# str_2 = list(input())
#
# dp = [[0] * (len(str_2) + 1) for _ in range(len(str_1) + 1)]
#
# for i in range(1, len(str_1) + 1):
#     for j in range(1, len(str_2) + 1):
#         if str_1[i - 1] == str_2[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#
# print(dp[len(str_1)][len(str_2)])

# 전깃줄

# N = int(input())
#
# arr = [list(map(int, input().split())) for _ in range(N)]
# arr.sort(key=lambda x: x[0])
#
# dp = [1] * N
#
# for i in range(N):
#     for j in range(i):
#         if arr[i][1] > arr[j][1]:
#             dp[i] = max(dp[i], dp[j] + 1)
#
# print(N - max(dp))

# 백준 2589 보물섬

# todo : bfs 함수 (육지로 최단거리)
# todo : 메인 부분 (2중 for문으로 출발지, 도착지 다 돌기)

# from collections import deque
#
#
# def bfs(x, y):
#     queue = deque([(x, y)])
#     visited[x][y] = 1
#
#     while queue:
#         nx, ny = queue.popleft()
#
#         dx = [-1, 1, 0, 0]
#         dy = [0, 0, -1, 1]
#
#         for idx in range(4):
#             cx = nx + dx[idx]
#             cy = ny + dy[idx]
#             if 0 <= cx < N and 0 <= cy < M and arr[cx][cy] == 'L' and visited[cx][cy] == 0:
#                 queue.append((cx, cy))
#                 visited[cx][cy] = visited[nx][ny] + 1
#
#     return max(map(max, visited))
#
#
# N, M = map(int, input().split())
#
# arr = [list(input()) for _ in range(N)]
#
# max_time = 0
#
# for i in range(N):
#     for j in range(M):
#         visited = [[0] * M for _ in range(N)]
#         if arr[i][j] == 'L':
#             now_time = bfs(i, j)
#             if now_time > max_time:
#                 max_time = now_time
#
# print(max_time - 1)

# 백준 14502 연구소

# todo : 벽 3개 모든 경우의 수 구하기 (def)
# todo : 각 경우의 수의 지도에서 모든 2 bfs
# todo : (메인) bfs 완료한 지도에서 안전 영역 크기 구하기

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(M)]
#
# empty_area = []
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             empty_area.append((i, j))
#
#
#
# def build_walls(count_walls, start):
#     if count_walls == 4:
#         return


# build_walls()

# 백준 5014 스타트링크

# from collections import deque
#
# F, S, G, U, D = map(int, input().split())
#
# visited = [0] * (F + 1)
#
# # 연결 그래프를 어떻게 받지? up down 밖에 없는데
# # visited 배열은 1차원이면 되나?
#
#
# def bfs(start_node):
#     queue = deque([S])
#     visited[start_node] = 1
#
#     while queue:
#         current_floor = queue.popleft()
#
#         if current_floor == G:
#             return visited[current_floor] - 1
#
#         upper, lower = current_floor + U, current_floor - D
#         for next_floor in (upper, lower):
#             if 1 <= next_floor <= F and visited[next_floor] == 0:
#                 visited[next_floor] = visited[current_floor] + 1
#                 queue.append(next_floor)
#
#     return "use the stairs"
#
#
# result = bfs(S)
# print(result)

# 백준 1697 숨바꼭질

# 최단 시간 -> bfs

# from collections import deque
#
# N, K = map(int, input().split())
#
# visited = [0] * 100001
#
#
# def bfs(start_node):
#     queue = deque([N])
#     visited[N] = 1
#
#     while queue:
#         now = queue.popleft()
#         next_step_list = [now + 1, now - 1, now * 2]
#
#         for next_step in next_step_list:
#             if 0 <= next_step <= 100000 and visited[next_step] == 0:
#                 visited[next_step] = visited[now] + 1
#                 queue.append(next_step)
#
# bfs(N)
# print(visited[K] - 1)

# 백준 3055 탈출

# 최소 시간 -> bfs

# 물도 bfs 돌면서 채우고, 고슴도치는 물 채워진 후에 가능한 최선의 방향 선택

# 1. 현재의 모든 물 칸 좌표 get -> 상하좌우 *로 바꿔주고 물 리스트에 좌표 추가해주기
# 2. 고슴도치 상하좌우 체크해서 범위 안이고 방문 안했고 물이 아니고 돌이 아니면 visited = 이전 visited + 1, queue에 append
# * 만약에 체크했는데 == D 이면, return visited 값

from collections import deque

R, C = map(int, input().split())
forest_map = [list(input()) for _ in range(R)]

water_queue = deque([])

for i in range(R):
    for j in range(C):
        if forest_map[i][j] == "*":
            water_queue.append((i, j))




def bfs():
    pass


for x, y in water_queue:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= R and 0 <= ny <= C and forest_map[nx][ny] == '.':
            forest_map[nx][ny] = '*'
            water_queue.append((nx, ny))