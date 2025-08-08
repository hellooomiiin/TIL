import sys
sys.stdin = open("input.txt")

# 파리 퇴치
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

# 리스트 컴프리헨션 list[i, i + 1] for _ in range()
# N - M -1 로 for문 돌아야 할 듯
# 델타로 풀 수 없음


# 바이러스 죽이기

T = int(input())

for tc in range(1, T + 1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    s = 0
    max_sum = 0
    dir_idx = 0

    for i in range(N):
        for j in range(N):
            s = arr[i][j]

            for dir_idx in range(4):
                for m in range(1, P + 1):
                    # 우 하 좌 상
                    di = [0, 1, 0, -1]
                    dj = [1, 0, -1, 0]

                    ni = i + m * di[dir_idx]
                    nj = j + m * dj[dir_idx]

                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]

            if s > max_sum:
                max_sum = s

    print(f'#{tc} {max_sum}')

    # arr을 쫙 돌면서
    # 좌표 i, j일 때 본인 값 sum에 먼저 더하고, 바깥에서는 방향 4가지 돌고 안에서는 P번 동안 하나씩 증가해서 나오는 모든 좌표의 값을 다 sum에 넣어줘야 함
    # 근데 조건 = 벽을 만나면 끝
    # 변수 설정해서 더 큰 게 나오면 더 큰 sum 을 max_sum으로 저장

# 사다리

T = 10

for tc in range(1, 11):
    tc_num = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 출발점(value == 2) 찾기
    for i in range(100):
        if arr[99][i] == 2:
            start_idx = i
            # print(start_idx)

    # 방향 설정 (우좌상)
    di = [0, 0, -1]
    dj = [1, -1, 0]

    i, j = 99, start_idx
    dir_i = 2

    # 동작 구현
    # 출발점이 값이 있을 때, 새로운 위치는 위로 한 칸
    while arr[i][j]:
        ni, nj = i + di[dir_i], j + dj[dir_i]

        if i, j 왼쪽이 1이라면:
            왼쪽끝까지 이동


        i = ni
        j = nj
        if


    # 99, start_ind = 출발점
    # 기본적으로 출발점에서 위로 한 칸씩 올라가는데,
    # 현재 좌표의 좌우 중 1이 있다면 -> 그 방향으로 전환해서 한 칸씩 전진
    # 전진하려는데 그 칸이 0이거나 밖이면 다시 위로 전진
    # arr 0행 도착할 때까지 반복, 도착하면 종료
    # 도착했을 때 (0, ?) 의 ? 반환

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


    # 가능한 출발 지점 리스트 (필요 X)
    pos_start = []
    for i in range(100):
        if arr[0][i] == 1:
            pos_start.append(i)
            print(pos_start)

    # 밑에서부터 올라오도록 구현
    while문, 종료 조건 : y 좌표가 0일 때까지 조건 만족할 때까지 돌아야 함

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
