# https://www.acmicpc.net/problem/21734
# 2025-04-25 / 21734. SMUPC의 등장 / Bronze II

# 이딴식으로 풀면 뺨 맞기 딱 좋다
print("\n".join(c * sum(map(int, str(ord(c)))) for c in input()))
