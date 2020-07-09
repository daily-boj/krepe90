# https://www.acmicpc.net/problem/5015
# 2020-07-09 / 5015. ls / Gold III

# ################## 틀렸습니다
# import sys
# P = sys.stdin.readline().rstrip()
# N = int(input())
# for i in range(N):
#     F = sys.stdin.readline().rstrip()
#     # 왼쪽끝과 오른쪽끝이 와카가 아닐때 일치하는지 여부
#     non_wc = P.split("*")
#     min_idx = 0
#     for w in non_wc[:-1]:
#         idx = F.find(w, min_idx)
#         if idx == -1:
#             break
#         # print(idx)
#         min_idx = idx + len(w)
#     else:
#         # 마지막이 일치하지 않는 경우
#         if non_wc[-1] and non_wc[-1] != F[-len(non_wc[-1]):]:
#             continue
#         print(F)


# ################## 시간 초과. 재귀 써서 그런가봄
# import sys
# import re
# def search(L: list, pos: int, prev: int, length: int):
#     if pos == len(L):
#         return prev == length
#     for st, ed in L[pos]:
#         if prev <= st:
#             res = search(L, pos + 1, ed, length)
#             if res:
#                 return True
#         else:
#             pass
#     # print(f"{pos}: {res}")
#     return False
# P = sys.stdin.readline().rstrip()
# P = re.sub("[*]+", "*", P)
# non_wc = P.split("*")
# # non_wc_orig = P.split("*")
# # non_wc = [n for n in non_wc_orig]
# # non_wc_len = [len(n) for n in P]
# N = int(input())
# for i in range(N):
#     F: str = sys.stdin.readline().rstrip()
#     pos_list = []
#     for w in non_wc:
#         idx = 0
#         pos = []
#         while True:
#             x = F.find(w, idx)
#             if x == -1:
#                 break
#             pos.append((x, x + len(w)))
#             idx = x + len(w) if w else x + 1
#         pos_list.append(pos)
#     # print(pos_list)
#     if search(pos_list, 0, 0, len(F)):
#         print(F)


##############
import sys
import re
P = sys.stdin.readline().rstrip()
P = re.sub("[*]+", "*", P)
non_wc = P.split("*")
N = int(input())
for i in range(N):
    F = sys.stdin.readline().rstrip()
