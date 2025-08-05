import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    seq = input()

    count = 0
    max_count = 0

    for ch in seq:
        if ch == "1":
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

    print(f'#{tc} {max_count}')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    dat = [0] * 5

    while N % 11 == 0:
        dat[4] += 1
        N //= 11
    while N % 7 == 0:
        dat[3] += 1
        N //= 7
    while N % 5 == 0:
        dat[2] += 1
        N //= 5
    while N % 3 == 0:
        dat[1] += 1
        N //= 3
    while N % 2 == 0:
        dat[0] += 1
        N //= 2

    print(f'#{tc}', end=' ')
    for num in dat:
        print(num, end=' ')
    print()

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    seq = input()
    dat = [0] * 10
    for number in seq:
        int_num = int(number)
        dat[int_num] += 1
        max_number = max(dat)
    max_number = 0
    max_card = 0
    for i in range(10):
        if dat[i] >= max_number:
            max_number = dat[i]
            max_card = i
    print(f'#{tc} {max_card} {max_number}')

for i in dat:
    max_card = 0
    if i >= max_card:
        max_card = dat.index(i)
    max_card_value = 0
    max_card_index = 0
    for i in range(10):

        if dat[i] >= max_card_value:
            max_card_value = dat[i]
            max_card_index = i
    print(f'#{tc} {max_card_index} {max_card_value}')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split(' ')))
    min_num = 10
    for i in range(N - 1):
        if li[i] < min_num:
            min_num = li[i]
            min_num_index = i
    max_num = 0
    max_num_index = 0
    for i in range(N - 1):
        if li[i] >= max_num:
            max_num = li[i]
            max_num_index = i

    print(f'#{tc} {max_num_index - min_num_index}')

    for i in range(10):
#         if dat[i] >= max_number:
#             max_number = dat[i]
#             max_card = i


    for num in li:
        if num >= max_num:
            max_num = num
            max_num_index = li.index(num)