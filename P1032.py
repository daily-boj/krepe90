# https://www.acmicpc.net/problem/1032
# 2021-06-29 / 1032. 명령 프롬프트 / Bronze I

# 문자열의 길이가 같다
N = int(input())
name = []
for i in range(N):
    if not name:
        name = list(input())
    else:
        new_name = input()
        for j, c in enumerate(new_name):
            if name[j] == "?":
                continue
            if name[j] != c:
                name[j] = "?"
print("".join(name))
