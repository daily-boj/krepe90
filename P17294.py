# https://www.acmicpc.net/problem/17294
# 2020-06-30 / 17294. 귀여운 수~ε٩(๑> ₃ <)۶з / Bronze I
x = list(map(int, input()))
a = x[0]
d = x[1] - x[0] if len(x) > 1 else 0
for i, c in enumerate(x):
    if c != a + d * i:
        print("흥칫뿡!! <(￣ ﹌ ￣)>")
        break
else:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
