# https://www.acmicpc.net/problem/1406
# 2025-04-30 / 1406. 에디터 / Silver II

# L     커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D     커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B     커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
#       삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $   $라는 문자를 커서 왼쪽에 추가함

# Python 기본 list 타입은 linked list가 아니다
# 직접 구현하긴 귀찮으니 스택 두개를 사용하는게 좋을 것 같다.
#   켜서 왼쪽, 오른쪽 각각 별도의 스택으로.

import sys
input = lambda: sys.stdin.readline().rstrip()
print = sys.stdout.write

s = input()
M = int(input())

left = []
right = []
left.extend(s)
for _ in range(M):
    cmd = input()
    match cmd:
        case "L":
            if not left:
                continue
            right.append(left.pop())
        case "D":
            if not right:
                continue
            left.append(right.pop())
        case "B":
            if not left:
                continue
            left.pop()
        case _:
            left.append(cmd[-1])
print("".join(left) + "".join(right[::-1]))
