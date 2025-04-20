# https://www.acmicpc.net/problem/19949
# 2025-04-20 / 19949. 영재의 시험 / Silver II

# 정직하게 완전탐색 문제인듯...
# 1천만번이면 할만하긴 하지만 좀 느리다.
# 풀긴 했지만 더 좋은 방법이 없을까?

# 다른 사람 풀이를 봤는데 3차원 DP를 시전하고 있다.
# 시간이 많으면 느긋하게 이해해보겠는데, 아쉽게도 그럴 시간은 지금 없기 때문에
#  기회가 된다면 해보는걸로...

ans = list(map(int, input().split()))

def dfs(arr: list, depth: int, ans_cnt=0):
    if depth >= 10:
        return 1 if ans_cnt > 4 else 0

    cnt = 0
    for i in range(1, 6):
        arr[depth] = i
        if depth > 1 and arr[depth-2] == arr[depth-1] == i:
            continue
        if arr[depth] == ans[depth]:
            new_ans_cnt = ans_cnt + 1
        else:
            new_ans_cnt = ans_cnt
        cnt += dfs(arr, depth + 1, new_ans_cnt)
    return cnt

print(dfs([0] * 10, 0, 0))
