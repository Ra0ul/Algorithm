answer = []

for i in range(0, 10):
    num = int(input())
    answer.append(num % 42)
answer = set(answer)

print(len(answer))