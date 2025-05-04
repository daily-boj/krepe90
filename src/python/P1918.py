# https://www.acmicpc.net/problem/1918
# 2025-05-04 / 1918. 후위 표기식 / Gold II

# 0. 연산자를 임시로 저장해두는 stack 스택, 결과를 저장하는 result 리스트 선언
# 1. `(` -> push
# 2. `)` -> `(` 직전까지 pop 해서 result.append, `(`는 버리기
# 3. 이 외 연산자 -> 자신보다 낮은 우선순위의 연산자 or 괄호 열기가 나오기 전까지 pop
#    이후 push
# 4. 종료 직전 stack 털어주기

s = input()

stack = []
result = []
for c in s:
    if c == "(":
        stack.append("(")
    elif c == ")":
        while stack:
            op = stack.pop()
            if op == "(":
                break
            result.append(op)
    elif c in "*/":
        while stack and stack[-1] not in "+-(":
            result.append(stack.pop())
        stack.append(c)
    elif c in "+-":
        while stack and stack[-1] != "(":
            result.append(stack.pop())
        stack.append(c)
    else:
        result.append(c)

while stack:
    result.append(stack.pop())
print(*result, sep="")
