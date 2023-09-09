from sys import stdin

input = stdin.readline
new_set = list(map(int, input().split()))
full_set = [1, 1, 2, 2, 2, 8]
answer = []

for i in range(len(new_set)):
    need = full_set[i] - new_set[i]
    answer.append(need)

print(*answer)