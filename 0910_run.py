import sys
sys.stdin = open("input.txt")

# arr = [4, 2, 23, 11, 7, 9, 19]
#
# arr.sort()
#
#
# def binary_search(target):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == target:
#             return
#         if target < arr[mid]:
#             right = mid - 1
#         if target > arr[mid]:
#             left = mid + 1
#
#
# binary_search(7)

# T = int(input())
#
# for tc in range(1, T + 1):
#     strs = input().strip()
#
#     def binary_search(arr):
#         left = 0
#         right = len(arr) - 1
#
#         while left <= right:
#             mid = (left + right) // 2
#
#             if arr[mid] == '#':
#                 left = mid + 1
#
#             else:
#                 right = mid - 1
#         return left * 100 / len(arr)
#
#     result = int(binary_search(strs))
#     print(f'#{tc} {result}%')

# T = int(input())
#
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     arr = [int(input()) for _ in range(N)]
#
#     def test():
#         pass
#
#     def binary_search():
#         left = 0
#         right = max(arr)
#
#         while left <= right:
#             mid = (left + right) // 2
#
#             if test(mid):
#                 left = mid - 1
#
#
#     binary_search()

# 1~10 부분집합 합이 10인 애들 출력하기

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def recur(n):
#     if
#     path = []
#     path.append(n)
#
#     recur(n + 1)
#
#
# recur(1)

# 백준 10810

# N, M = map(int, input().split())
# bucket = [0] * N
# arr = [list(map(int, input().split())) for _ in range(M)]
#
# for i in range(M):
#     for j in range(arr[i][0], arr[i][1] + 1):
#         bucket[j - 1] = arr[i][2]
#
# print(*bucket)

# 백준 10813

# N, M = map(int, input().split())
#
# bucket = []
# check = []
#
# for num in range(1, N + 1):
#     bucket.append(num)
#     check.append(num)
#
# arr = [list(map(int, input().split())) for _ in range(M)]
#
# for i in range(M):
#     bucket[arr[i][0] - 1] = check[arr[i][1] - 1]
#     bucket[arr[i][1] - 1] = check[arr[i][0] - 1]
#     check[arr[i][1] - 1] = bucket[arr[i][1] - 1]
#     check[arr[i][0] - 1] = bucket[arr[i][0] - 1]
#
# print(*bucket)

# 백준 10870

# n = int(input())
#
# arr = [0] * (n + 2)
#
# arr[0] = 0
# arr[1] = 1
#
#
# def recur(num):
#     if num == n + 2:
#         print(arr[n])
#         return
#     arr[num] = arr[num - 1] + arr[num - 2]
#     recur(num + 1)
#
#
# recur(2)

# 백준 10829

# N = int(input())
# result = []
#
# def binary(n):
#     if n == 1:
#         result.append(1)
#         return
#     if n == 2:
#         result.append(0)
#         result.append(1)
#         return
#     result.append(n % 2)
#     binary(n // 2)
#
#
# binary(N)
# for i in result[::-1]:
#     print(i, end='')

# 백준 25501

# T = int(input())
#
# for tc in range(1, T + 1):
#     my_str = input()
#
#     c = 1
#
#     def recursion(s, l, r):
#         global c
#         if l >= r:  # r이 0과 같거나 작을 때
#             return 1
#         elif s[l] != s[r]:
#             return 0
#         else:
#             c += 1
#             return recursion(s, l + 1, r - 1)
#
#
#     def isPalindrome(s):  # s는 문자열
#         return recursion(s, 0, len(s) - 1)  # recursion(문자열, 0, 문자열 길이 - 1)
#
#
#     print(isPalindrome(my_str), c)

# 백준 9506

# import math
#
# while True:
#     n = int(input())
#
#     if n < 0:
#         break
#
#     numbers = []
#
#     def recur(num):
#         if num == int(math.sqrt(n)) + 1:
#             return
#         if n % num == 0:
#             numbers.append(num)
#             recur(num + 1)
#         else:
#             recur(num + 1)
#     recur(1)
#
#     half = []
#
#     for i in numbers:
#         half.append(n // i)
#
#     total = list(set(numbers + half))
#     total.sort()
#     total.pop()
#
#     if n == sum(total):
#         print(f'{n} =', end=' ')
#         answer = ' + '.join(map(str, total))
#         print(answer)
#     else:
#         print(f'{n} is NOT perfect.')

# 백준 17478

# N = int(input())
# sens = ['"재귀함수가 뭔가요?"', '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.', '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.', '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."']
#
#
# def recur(num):
#     if num == N:
#         print(num * 4 * '_', end='')
#         print(sens[0])
#         print(num * 4 * '_', end='')
#         print('"재귀함수는 자기 자신을 호출하는 함수라네"')
#         print(num * 4 * '_', end='')
#         print('라고 답변하였지.')
#         return
#
#     for sen in sens:
#         print(num * 4 * '_', end='')
#         print(sen)
#     recur(num + 1)
#     print(num * 4 * '_', end='')
#     print('라고 답변하였지.')
#
#
# print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
# recur(0)

# 백준 9095

# T = int(input())
#
# for tc in range(1, T + 1):
#     n = int(input())

# BFS 기초 - 방문 순서 출력하기

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 인접행렬
    graph = [list(map(int, input().split())) for _ in range(N)]

    def bfs(start):
        # 앞으로 방문해야 할 리스트
        dq = deque([start])  # 시작 노드를 큐에 추가

        while dq:
            now = dq.popleft()
            print(now, end='')





    bfs(0)
