# https://www.acmicpc.net/problem/2217
# 2024-11-07 / 2217. 로프 / Silver IV

# 1. 전체 로프 정보 입력받기
ropes = [int(input()) for _ in range(int(input()))]
# 2. 내림차순 정렬
ropes.sort(reverse=True)
# 3. 최대 중량 구하기
# 내림차순 정렬 상태에서 '1번째 + ... + n번째 로프'가 들 수 있는 최대 무게는 'n번째 로프 최대하중 * n'과 같음.
max_weight = 0
for i, rope in enumerate(ropes):
    max_weight = max(max_weight, rope * (i + 1))
# 4. 출력
print(max_weight)
