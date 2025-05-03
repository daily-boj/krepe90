# https://www.acmicpc.net/problem/15312
# 2025-05-03 / 15312. 이름 궁합 / Silver V

# 두 문자열을 교차해서 더하는 깔끔한 방법이 뭐가 있을까
# 잘 모르겠다...

m = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
s1 = input()
s2 = input()
arr = [-1] * (len(s1) * 2)

for i in range(len(s1)):
    arr[i * 2] = m[ord(s1[i]) - 65]
    arr[i * 2 + 1] = m[ord(s2[i]) - 65]

while len(arr) > 2:
    arr = [(x + y) % 10 for x, y in zip(arr[:-1], arr[1:])]
print(*arr, sep="")
