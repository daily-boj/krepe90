# https://www.acmicpc.net/problem/16561
# 2025-03-17 / 16561. 3의 배수 / Bronze II

#  (*3)
# 3 -> 1
# 4 -> 3 (+2)
# 5 -> 6 (+3)
# 6 -> 10 (+4)
# 7 -> 15 (+5)
# 5 * 4 / 2
# 6 * 5 / 2

n = int(input()) // 3
print(((n - 1) * (n - 2)) // 2)
