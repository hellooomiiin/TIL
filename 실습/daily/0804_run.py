N = int(input())
input().split()







T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))

    result = max(li) - min(li)

    print(f'#{tc} {result}')







T = int(input())
N



T = int(input())

for tc in range(1, T + 1):
    H, W = list(map(int, input().split()))
    table = [list(map(int, input().split())) for _ in range(H)]

table = {}
for i in table:
    if table.get(i):
        table[i] += 1
    else:
        table[i] = 1
return table

dat = [0] * 10000001

for i in range(H):
    for j in range(W):
        number = table[i][j]
        dat[number] += 1

print(f'#{tc} {dat.index(max(dat))}')

if max_count < dat[number]:
    max_count = dat[number]

dat[65000] += 1
dat[35] += 1
dat[42] += 1

dat.index(max(dat))






T = int(input())

for tc in range(1, T + 1):
    AH, AW = map(int, input().split())

    # 아파트 기준으로 dat를 만든다.
    dat = [0] * 100001

    for _ in range(AH):
        row = list(map(int, input().split()))
        for num in row: # 15 42 65 60
            dat[num] += 1

    # A_table = [list(map(int, input().split())) for _ in range(AH)]

    blacklist_count = 0
    BH, BW = map(int, input().split())
    for _ in range(BH):
        row = list(map(int, input().split()))
        for num in row: # 15 5 4
            blacklist_count += dat[num]
            dat[num] = 0 # 중복계산 방지용

    normal_count = (AH * AW) - blacklist_count
    print(f'#{tc} {blacklist_count} {normal_count}')

    B_table = [list(map(int, input().split())) for _ in range(BH)]


    for i in AH:
        for j in AW:
            print(A_table[i][j])

        for j in B_table:
            if A_table.get(i):
                A_table[i] += 1



print(f'#{tc} {)}')


T = int(input())

for tc in range(1, T + 1):
    H, W = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(H)]

    dat = [0] * 10000001

    max_count = 0
    max_index = 10000000

    for i in range(H):
        for j in range(W):
            number = table[i][j]
            dat[number] += 1

            if max_count < dat[number]:
                max_count = dat[number]
                max_index = number

            if dat[max_index] == max_count and number < max_index:
                max_index = number

print(f'#{tc} {max_index}')



T = int(input())

for tc in range(1, 51):
    N, M = list(map(int, input().split()))
    li = list(input())

    li.sort()
    print(li.sort)