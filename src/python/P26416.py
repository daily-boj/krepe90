# https://www.acmicpc.net/problem/26416
# 2025-03-23 / 26416. New Password / Bronze II

# 비밀번호 조건:
#   - 7자 이상
#   - 알파벳 대문자 1개 이상
#   - 알파벳 소문자 1개 이상
#   - 숫자 1개 이상
#   - 특수문자 1개 이상, 단 특수문자는 '#@*&' 4개
# (구) 비밀번호가 지키지 못한 조건들을 지킬 수 있도록 추가해주면 되는 문제

T = int(input())

for x in range(T):
    pw_len = int(input())
    pw = input()

    for c in pw:
        if ord("a") <= ord(c) <= ord("z"):
            break
    else:
        pw += "a"

    for c in pw:
        if ord("A") <= ord(c) <= ord("Z"):
            break
    else:
        pw += "A"
    
    for c in pw:
        if ord("0") <= ord(c) <= ord("9"):
            break
    else:
        pw += "1"
    
    for c in pw:
        if c in "#@*&":
            break
    else:
        pw += "*"

    print(f"Case #{x + 1}: {pw:<07s}")
