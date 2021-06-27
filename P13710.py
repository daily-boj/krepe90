# https://www.acmicpc.net/problem/13710
# 2020-07-10 / 13710. XOR 합 3 / Gold I

# 시간 초과, O(N^2)
# import array
# N = int(input())
# A = array.array("I", map(int, input().split()))
# S = array.array("I", A)
# result = sum(S)
# for i in range(1, N):
#     head, tail = i, 0
#     while head < N:
#         S[tail] ^= A[head]
#         result += S[tail]
#         head += 1
#         tail += 1
# print(result)


# 비트 단위로 계산 (DP)
import array
N = int(input())
A = array.array("I", map(int, input().split()))
result = 0
for bit in range(32):
    mask = 1 << bit
    cnt_all = 0
    cnt_one = 0
    for i in range(N):
        # 1의 개수를 셈
        if mask & A[i]:
            cnt_one = i - cnt_one + 1
        cnt_all += cnt_one
    result += cnt_all << bit
print(result)
