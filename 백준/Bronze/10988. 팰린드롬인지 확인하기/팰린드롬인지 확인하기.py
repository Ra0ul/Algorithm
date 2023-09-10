word = input()
half_length = len(word) // 2
answer = 1

for i in range(half_length):
    if word[i] != word[-(i + 1)]:
        answer = 0

print(answer)