import sys
sys.stdin = open("input.txt")

# 1

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    fin_i, fin_j = -1, -1

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            c = 0
            for x in range(M):
                for y in range(M):
                    for_i = i + x
                    for_j = j + y
                    if 0 <= for_i < N and 0 <= for_j < N:
                        if arr[for_i][for_j] == '*':
                            c += 1
            if c == K:
                fin_i, fin_j = i, j
                break

    print(f'#{tc} {fin_i} {fin_j}')

# 2 (델타)

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    s = 0

    for i in range(1, N):
        for j in range(M):
            # 우 하 좌 상
            di = [0, 1, 0, -1]
            dj = [1, 0, -1, 0]
            for idx in range(4):
                ni, nj = i + di[idx], j + dj[idx]
                # 범위에 들어오면 일단 가운데랑 비교, 안들어오면 pass, 비교해서 ninj가 더 크면 pass
                # 문제 없으면 다 돌아서 확인하고 + 1
                if 0 <= ni < N and 0 <= nj < M:
                    continue
                if arr[ni][nj] < arr[i][j]:
                    break
                else:
                    s += 1
    print(f'#{tc} {s}')