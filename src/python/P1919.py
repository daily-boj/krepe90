# https://www.acmicpc.net/problem/1919
# 2025-04-11 / 1919. 애너그램 만들기 / Bronze II

# 두 단어에서 겹치지 않는 글자들을 빼기
# 단어 A의 알파벳별 글자 i의 합계를 a[i] 라고 할 때, abs(a[i] - b[i]) 한거의 합을 구하면 될듯.

import sys
input = lambda: sys.stdin.readline().rstrip()


def count(s):
    arr = [0] * 26
    for c in s:
        arr[ord(c) - 97] += 1
    return arr

A = input()
B = input()
print(sum(abs(a - b) for a, b in zip(count(A), count(B))))
