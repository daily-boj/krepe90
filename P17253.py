# https://www.acmicpc.net/problem/17253
# 2020-06-10 / Silver II
# pow(2, 63) - 1보다 작은 pow(3, 39)부터 시작
# x를 p로 뺄 수 있으면 (x >= p) 그만큼 빼준다.
# 이때 p가 pow(3, i) 라면 해당 정수는 3의 i제곱을 가지고 있다는 뜻.
# 최종적으로 x == 0이 되면 해당 수는 "삼삼한 수"가 된다. 0이 아니라면 3의 제곱수로만 이루어진 수가 아닌것
# 하지만 입력값이 0일때는 삼삼한 수가 아니므로 이에 대한 예외처리도 해줘야함.
x = int(input())
if x == 0:
    print("NO")
else:
    for i in range(39, -1, -1):
        p = pow(3, i)
        if x >= p:
            x = x - p
    print("YES" if x == 0 else "NO")
