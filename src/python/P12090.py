# https://www.acmicpc.net/problem/12090
# 2020-07-08 / 12090. 초성 변환 / Bronze I
M = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
print("".join(map(lambda x: M[(ord(x) - 0xAC00) // 588], input())))
