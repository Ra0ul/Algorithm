from sys import stdin

input = stdin.readline

cro_alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input().rstrip()
answer = 0

# 크로아티아 알파벳 빼기
for i in cro_alpha:
    while i in word:
        if i in word:
            num = word.index(i)
            answer += 1
            word = word[:num] + " " + word[num + len(i) :]

# 혹시 =, - 가 남아 있으면 빼줘라
if "=" in word or "-" in word:
    try:
        num = word.index("=")
    except:
        num = word.index("-")
    word = word[:num] + " " + word[num + 1 :]

word = "".join(word.strip().split())
print(answer + len(word))