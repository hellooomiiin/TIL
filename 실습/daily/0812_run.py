import sys
sys.stdin = open("input.txt")

# 괄호 짝짓기

# T = 10
# for tc in range(1, 11):
#     N = int(input())
#     arr = list(input())
#
#     stack = []
#
#     found = True
#
#     for i in arr:
#         if i == ')':
#             if len(stack) > 0 and stack[-1] == '(':
#                 stack.pop()  # 인덱스를 지정하지 않고 stack.pop()만 호출하면 리스트의 맨 마지막 요소를 제거하기만 함
#             else:
#                 found = False
#                 break
#         elif i == ']':
#             if len(stack) > 0 and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 found = False
#                 break
#         elif i == '}':
#             if len(stack) > 0 and stack[-1] == '{':
#                 stack.pop()
#             else:
#                 found = False
#                 break
#         elif i == '>':
#             if len(stack) > 0 and stack[-1] == '<':
#                 stack.pop()
#             else:
#                 found = False
#                 break
#         else:
#             stack.append(i)
#
#     if len(stack) > 0:
#         found = False
#
#     print(f'#{tc} 1' if found else f'#{tc} 0')

# 여는 괄호 -> stack 쌓기
# 닫는 괄호 -> stack 비어있지 않고 stack 맨 윗 값 확인해서 같으면 stack pop

# 왜 stack[-1]이지? -> list[-1]은 맨 마지막 인덱스 값이니까 스택 가장 위 숫자

# 비밀번호

T = 10
for tc in range(1, 11):
   str_N, str_arr = input().split()
   N = int(str_N)
   arr = list(str_arr)
   stack = []

   for i in arr:
       stack.append(i)  # 숫자 stack에 넣기
       if i + 1 == stack[-1]:  # i + 1 값 맨 위 스택 숫자와 같으면?
           stack.pop()
           arr.pop(i)  # 스택 맨 윗 값 pop arr i 값도 pop
       else:
           i += 1

# arr을 하나씩 돌면서, 일단 stack에 값 저장, 그리고 다음 값과 방금 저장한 값 일치하는지 확인, 일치하면 둘 다 pop, 불일치하면 다음꺼 돌기