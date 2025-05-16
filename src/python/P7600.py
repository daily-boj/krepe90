# https://www.acmicpc.net/problem/7600
# 2025-05-17 / 7600. 문자가 몇갤까 / Bronze II

# 이런식으로 풀면 뺨맞기 딱 좋을듯

while True:
    s = input()
    if s == "#":
        break
    print(len(set(s.lower()) & set("abcdefghijklmnopqrstuvwxyz")))

# 이건 깔끔하긴 한데 느리고

# import re
# while (s := input().lower()) != "#":
#     print(len(set(re.sub(r"[^a-z]", "", s))))
