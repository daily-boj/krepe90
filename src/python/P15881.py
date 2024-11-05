# https://www.acmicpc.net/problem/15881
# 2021-06-28 / 15881. Pen Pineapple Apple Pen / Bronze II

# 1.
# 주의해야 하는 TC: pPApPAP, pppPAp, pPPApPAp 등.
_ = input()
S = input()
cnt = 0
stat = 0
for c in S:
    if stat < 3 and c == "p":
        stat = 1
    elif stat == 1 and c == "P":
        stat = 2
    elif stat == 2 and c == "A":
        stat = 3
    elif stat == 3 and c == "p":
        stat = 0
        cnt += 1
    else:
        stat = 0
print(cnt)
