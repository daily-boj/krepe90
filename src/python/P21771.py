# https://www.acmicpc.net/problem/21771
# 2025-03-16 / 21771. 가희야 거기서 자는 거 아니야 / Bronze I

# 베개 위에서 자고 있다 == 베개가 조금이라도 가려진다
#   (베개 중의 일부가 가희에 의해서 가려진 상태라면, 가희는 베게 위에서 자고 있습니다.)
# 문제에서 가희와 베개의 가로세로 길이를 둘다 제공
# -> 베개 넓이와 배게 문자열 갯수를 비교

R, C = map(int, input().split())
Rg, Cg, Rp, Cp = map(int, input().split())

p_area = Rp * Cp
A = "".join(input() for _ in range(R))

print(1 if A.count("P") != p_area else 0)
