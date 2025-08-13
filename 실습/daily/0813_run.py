import sys
sys.stdin = open("input.txt")

# 카드1

# N = int(input())
#
# cards = [i for i in range(N, 0, -1)]
#
# while len(cards) > 1:
#     print(cards.pop(), end=' ')
#     num = cards.pop()
#     cards.insert(0, num)
#
# print(cards[0])

# 카드2

# N = int(input())
#
# cards = deque([i for i in range(1, N, N + 1)])
#
# cards.popleft()

# 재귀호출 (top-down) -> 위에서 뿌려주는 느낌 / 반복문 (bottom-up)

# 피보나치 수 5

# def fibonacci(n):
#     return

# 피보나치 수 2 (메모이제이션)

# 1, 2, 3 더하기
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#
#     target = 10
#     result = 0
#     def recur(total):
#         global result
#         if total == target:
#             return
#         recur(total + 1)
#         recur(total + 2)
#         recur(total + 3)

# 콜라츠 추측

T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    count = 0

    def recur(n):
        global count
        if n == 1:
            count += 1
            return
        if n % 2 == 0:
            count += 1
            n //= 2
            return recur(n)
        if n % 2 != 0:
            count += 1
            n = n * 3 + 1
            return recur(n)

    print(recur(n))