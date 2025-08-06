import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, 11):
    N = 100
    tc_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    i_max_sum = 0
    for i in range(N):
        i_sum = sum(arr[i])
        if i_sum > i_max_sum:
            i_max_sum = i_sum
    j_max_sum = 0
    for j in range(N):
        j_sum = 0
        for i in range(N):
            j_sum += arr[i][j]
        if j_sum > j_max_sum:
            j_max_sum = j_sum
    sum_1 = 0
    for i in range(N):
        sum_1 += arr[i][i]
    sum_2 = 0
    for i in range(N):
        sum_2 += arr[i][N - 1 - i]
    li = [i_max_sum, j_max_sum, sum_1, sum_2]
    max_max = max(li)
    print(f'#{tc} {max_max}')


        for j in range(N):
            s += arr[i][j]
            i_sum = s
    print(i_sum)

print(max_sum)

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 1. 델타 배열을 만드는 과정
    # - P 개의 입력으로 델타 배열을 초기화
    P = int(input())
    delta = [0] * (N + 1)
    for _ in range(P):
        start, end, cost = map(int, input().split())
        # 변화량을 기록
        delta[start] += cost
        delta[end + 1] -= cost

    # 2. 델타 배열을 활용하는 과정
    current_delta = 0  # 현재 변화량
    for i in range(N):
        current_delta += delta[i]
        arr[i] += current_delta

    print(f"#{tc} {' '.join(map(str, arr))}")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    s = 0
    ri = 0
    rj = 0

    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            if max_sum < s:
                max_sum = s
                ri = i
                rj = j
    print(f'#{tc} {max_sum} {ri} {rj}')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_result = 0
    ry, rx = 0, 0

    # 전체 이차원 리스트를 순회하면서
    for y in range(N):
        for x in range(N):
            # 상하좌우 값들을 더해준다.
            result = arr[y][x]  # 현재좌표

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                # 범위 밖으로 나가면, 해당 방향은 계산 X
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue

                result += arr[ny][nx]

            # 최대값 갱신
            if max_result < result:
                max_result = result
                ry = y
                rx = x

    print(f'#{tc} {max_result} {ry} {rx}')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 1. 델타 배열을 만드는 과정
    # - P 개의 입력으로 델타 배열을 초기화
    P = int(input())
    delta = [0] * (N + 1) # 하나 더 만들어둬야 함
    for _ in range(P):
        start, end, cost = map(int, input().split())
        # 변화량을 기록
        delta[start] += cost
        delta[end + 1] -= cost

    # 2. 델타 배열을 활용하는 과정
    current_delta = 0  # 현재 변화량
    for i in range(N):
        current_delta += delta[i]
        arr[i] += current_delta

    print(f"#{tc} {' '.join(map(str, arr))}")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()) for _ in range(N))]


